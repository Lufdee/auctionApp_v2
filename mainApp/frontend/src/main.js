import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
// import { ErrorService } from "./Services/ErrorService";
// import Vue from "vue";

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

import router from './router';


// Vue.config.productionTip = false;
// Vue.config.errorHandler = (error) => ErrorService.onError(error);

createApp(App).use(router).mount('#app')

