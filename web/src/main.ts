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
import WellImport from '@/components/well/import/WellImport.vue';
import PlotDialog from "@/components/plot/dialog/PlotDialog.vue";

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

app.component('PlotDialog', PlotDialog)
app.component('WellImport', WellImport)
app.mount("#app");
