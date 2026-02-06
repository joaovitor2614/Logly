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
import WellImport from '@/components/well/io/import/WellImport.vue';
import WellExport from '@/components/well/io/export/WellExport.vue';
import ConfirmDeleteAccountDialog from "@/components/account/ConfirmDeleteAccountDialog.vue";
import PlotDialog from "@/components/plot/dialog/PlotDialog.vue";
import LogPlotDialog from "@/components/plot/dialog/LogPlotDialog.vue";
import WellCalculatorDialog from "@/components/well/calculator/WellCalculatorDialog.vue"; 
import WellLogsTableDialog from "@/components/well/welllogs/WellLogsTableDialog.vue";

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
app.component('LogPlotDialog', LogPlotDialog)
app.component('WellCalculatorDialog', WellCalculatorDialog)
app.component('WellImport', WellImport)
app.component('WellExport', WellExport)
app.component('ConfirmDeleteAccountDialog', ConfirmDeleteAccountDialog)
app.component('WellLogsTableDialog', WellLogsTableDialog)
app.mount("#app");
