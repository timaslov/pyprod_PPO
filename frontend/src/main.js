import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router/'

import './style.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')

let errors = []

try {
    const response = await fetch('http://127.0.0.1:8001/api/web/v1/articles/index')
    const result = await response.json()
    console.log(result)
}
catch (error) {
    errors.push(error)
}