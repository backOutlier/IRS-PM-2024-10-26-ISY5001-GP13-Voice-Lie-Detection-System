import os
from moviepy.editor import *

# save path
target_folder = 'D:/audio_files/'
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# looping
for f_name in os.listdir('D:/Research_Exploration/上课资料/NUS/Semester1/Practice Module/Audio-Visual-Deception-Detection-DOLOS-Dataset-and-Parameter-Efficient-Crossmodal-Learning/AV-Data-Processing/AV Data Processing/videos'):
    f_path = os.path.join('D:/Research_Exploration/上课资料/NUS/Semester1/Practice Module/Audio-Visual-Deception-Detection-DOLOS-Dataset-and-Parameter-Efficient-Crossmodal-Learning/AV-Data-Processing/AV Data Processing/videos', f_name)
    video = VideoFileClip(f_path)
    audio = video.audio
    if audio is not None:
        # saving
        save_name = os.path.join(target_folder, f_name.split('.')[0] + '.wav')
        print(f"Saving audio to {save_name}")
        audio.write_audiofile(save_name)
    else:
        print(f"No audio found in {f_name}")
