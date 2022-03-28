import { createApp } from 'vue'
import App from './App.vue'
import router from "./router"
import store from "./store"
import ElementPlus from "element-plus"
import 'element-plus/dist/index.css'
import socket from "./utils/socket"
// import chat from "./utils/chat"


const app = createApp(App)
app.use(router);
app.use(store)
app.use(ElementPlus)
app.config.globalProperties.$socket = socket;
// app.config.globalProperties.$chat = chat;

app.mount('#app')
