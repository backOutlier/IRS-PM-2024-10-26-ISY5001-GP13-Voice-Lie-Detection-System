import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import PrimeVue from 'primevue/config'
import ConfirmationService from 'primevue/confirmationservice';
import Aura from '@primevue/themes/aura'
import axios from "axios"

const axiosInstance = axios.create({
    baseURL: 'http://localhost:8000/api', // Django API addr
});

const app = createApp(App);
app.use(PrimeVue, {
    theme: {
        preset: Aura
    }
});
app.use(ConfirmationService);
app.config.globalProperties.$axios = axiosInstance;

app.mount('#app');
