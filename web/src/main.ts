import { createApp } from "vue";
import Toast from "vue-toastification";
// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import "vue-toastification/dist/index.css";
import '@mdi/font/css/materialdesignicons.css'
import "./assets/main.css";

const vuetify = createVuetify({
  components,
  directives,
})


// Pinia
import { createPinia } from 'pinia'




import App from "./App.vue";
import { setupRouter } from "./router/router";




const app = createApp(App);

const piniaRootStoreInstance = createPinia()




app.use(piniaRootStoreInstance)
app.use(vuetify)
app.use(Toast);
setupRouter(app)


app.mount("#app");
