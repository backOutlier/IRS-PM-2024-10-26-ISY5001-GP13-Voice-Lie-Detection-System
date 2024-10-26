<template>
  <Card style="width: 30rem; overflow: hidden">
    <template #header>
      <img alt="user header" src="../assets/dd_header.jpg" />
    </template>
    <template #title> Deception Detection Based on ML </template>
    <template #content>
      <ConfirmDialog>
        <template #message>
          <div>
            <p>Deception: {{ isDeception }}.</p>
            <p>Deception Probability: {{ deceptionProbability }}.</p>
          </div>
        </template>
      </ConfirmDialog>
      <tapir-widget :time='1' :customUpload='recordUpload' audioFormat="WAV" buttonColor="#F1F3F4"/> 
      <p class='text-center' style="font-size: 16px; color: #6B7280; margin: 20px;">
        - or upload your own audio file -
      </p>
      <FileUpload 
        name="demo[]"
        :customUpload="true"
        @uploader="myUploader"
        :maxFileSize="10000000"
        accept="audio/*"
        :multiple="false"
      />
    </template>
  </Card>
</template>

<script>
import Card from 'primevue/card';
import FileUpload from 'primevue/fileupload';
import TapirWidget from 'vue-audio-tapir'
import 'vue-audio-tapir/dist/vue-audio-tapir.css';
import toWav from 'audiobuffer-to-wav';
import ConfirmDialog from 'primevue/confirmdialog';
export default {
  components: {
    Card,
    FileUpload,
    TapirWidget,
    ConfirmDialog,
  },
  data() {
    return {
      isDeception: 'NO',
      deceptionProbability: '0.5',
    };
  },
  methods: {
    async wavConvert(file) {
      console.log('convert to wav')
      const audioContext = new (window.AudioContext || window.webkitAudioContext)();
      const arrayBuffer = await file.arrayBuffer();
      const audioBuffer = await audioContext.decodeAudioData(arrayBuffer);
      const wavBuffer = toWav(audioBuffer);
      const wavBlob = new Blob([wavBuffer], { type: 'audio/wav' });
      const wavFile = new File([wavBlob], 'converted-audio.wav', {
        type: 'audio/wav',
        lastModified: Date.now(),
      });
      return wavFile;
    },
    sendToBackend(formData){
      this.$axios.post('http://localhost:8000/api/audiofiles/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(response => {
        console.log('upload success', response.data);
        this.displayResult(response.data)
      }).catch(error => {
        console.error('upload fail', error);
        this.displayResult('Sorry, something went wrong.') // TODO: handle error
      });
    },
    async recordUpload(blob) {
      try {
        console.log('upload recording')
        const formData = new FormData()
        formData.append('audio_file', blob, 'audio.wav')
        this.sendToBackend(formData)
        return true
      } catch (error) {
        console.log('recordUpload error')
        return false
      }
      // TODO: rm file
    },
    async myUploader(event) {
      console.log('upload audio file')

      let file = event.files[0];
      // console.log(file)
      if (!file.name.toLowerCase().endsWith('.wav'))
        file = await this.wavConvert(file)
      const formData = new FormData();
      formData.append('audio_file', file);
      this.sendToBackend(formData)
    },
    displayResult(result)
    {
      let msg = ''
      if (result['Predicted Label'] == 1)
        this.isDeception = 'NO'
      else
        this.isDeception = 'YES'
      let p = result['Deception Probability']
      this.deceptionProbability = (parseFloat(p) * 100).toFixed(2) + "%";
      console.log('display result')
      this.$confirm.require({
        header: 'Detection Result',
        icon: 'pi pi-info-circle',
        acceptProps: {
          label: 'Correct',
          severity: 'success',
          icon: 'pi pi-check',
        },
        rejectProps: {
          label: 'Wrong',
          severity: 'danger',
          icon: 'pi pi-times',
        },
        accept: () => {
          console.log('ok')
        },
        reject: () => {
          console.log('oh no')
        }
      });
    },
  }
};
</script>