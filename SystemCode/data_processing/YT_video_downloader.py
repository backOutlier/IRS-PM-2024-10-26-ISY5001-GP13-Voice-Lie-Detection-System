import sys
import os
from multiprocessing.pool import ThreadPool
from yt_dlp import YoutubeDL
import ffmpeg

class VidInfo:
    def __init__(self, yt_id, file_name, start_time, end_time, outdir):
        self.yt_id = yt_id
        self.start_time = float(start_time)
        self.end_time = float(end_time)
        self.out_filename = os.path.join(outdir, file_name + '.mp4')

def convert_to_seconds(time_str):
    """Convert time string MM:SS to seconds."""
    try:
        if ':' in time_str:
            minutes, seconds = time_str.split(':')
            result = int(minutes) * 60 + int(seconds)
            print(f"Converting {time_str} to {result} seconds")  # log
            return result
        else:
            result = int(time_str)
            print(f"Converting {time_str} to {result} seconds")  # log
            return result
    except ValueError as e:
        print(f"Error converting time: {e}")
        return None

def download(vidinfo):
    yt_base_url = 'https://www.youtube.com/watch?v='
    yt_url = yt_base_url + vidinfo.yt_id

    ydl_opts = {
        'format': '22/18',
        'quiet': True,
        'ignoreerrors': True,
        'no_warnings': True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            download_url = ydl.extract_info(url=yt_url, download=False)['url']
    except:
        return_msg = '{}, ERROR (youtube)!'.format(vidinfo.yt_id)
        return return_msg

    try:
        (
            ffmpeg
                .input(download_url, ss=vidinfo.start_time, to=vidinfo.end_time)
                .output(vidinfo.out_filename, format='mp4', r=25, vcodec='libx264',
                        crf=18, preset='veryfast', pix_fmt='yuv420p', acodec='aac', audio_bitrate=128000,
                        strict='experimental')
                .global_args('-y')
                .global_args('-loglevel', 'error')
                .run()
        )
    except:
        return_msg = '{}, ERROR (ffmpeg)!'.format(vidinfo.yt_id)
        return return_msg

    return '{}, DONE!'.format(vidinfo.yt_id)

if __name__ == '__main__':
    split = sys.argv[1]  # name of the destination folder
    csv_file = sys.argv[2]
    out_dir = split

    os.makedirs(out_dir, exist_ok=True)

    # bad file log
    bad_files = open('videos/bad_files_videos.txt', 'w')


    with open(csv_file, 'r') as f:
        lines = f.readlines()[1:]  # get rid of the first line
        lines = [x.strip().split(',') for x in lines]

        vidinfos = []
        for x in lines:
            start_time = convert_to_seconds(x[2])
            end_time = convert_to_seconds(x[3])
            if start_time is not None and end_time is not None:
                vidinfos.append(VidInfo(x[0], x[1], start_time, end_time, out_dir))
            else:
                print(f"Skipping entry due to invalid times: {x}")

    # Download
    results = ThreadPool(5).imap_unordered(download, vidinfos)
    cnt = 0
    for r in results:
        cnt += 1
        print(cnt, '/', len(vidinfos), r)
        if 'ERROR' in r:
            bad_files.write(r + '\n')
    bad_files.close()
