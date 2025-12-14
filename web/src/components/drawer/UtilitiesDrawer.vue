<script setup lang="ts">
import { useAuthStore, useDialogStore, useUserStore } from '@/stores';
import { useRouter } from 'vue-router';
import { PlotType } from '../plot/types';



const userStore = useUserStore()
const authStore = useAuthStore()
const dialogStore = useDialogStore()

const openDialogComponent = (componentName: string) => {
  dialogStore.openDialogWindow(componentName)
}
const openPlotDialog = (plotType: `${PlotType}`) => {
  dialogStore.openDialogWindow('PlotDialog', {plotType: plotType})
 
}
</script>

<template>

        <v-navigation-drawer
          theme="dark"
          permanent
          class="d-flex"
   
         
        >

          <v-list-item>Welcome {{ userStore.userInfo.name }}</v-list-item>
          <v-divider></v-divider>
  
          <v-list
            density="compact"
            nav
          >
         
            <v-list-item append-icon="mdi-file" class="mt-10 mb-10" @click="openDialogComponent('WellImport')">Import Well</v-list-item>
            <v-list-item append-icon="mdi-export" class="mt-10 mb-10" @click="openDialogComponent('WellExport')">Export Well</v-list-item>
            <v-list-item append-icon="mdi-calculator" class="mt-10 mb-10" @click="openDialogComponent('WellCalculatorDialog')">Well Calculator</v-list-item>
            <v-list-item append-icon="mdi-chart-scatter-plot" class="mt-10 mb-10" @click="openPlotDialog('scatter')">CrossPlot</v-list-item>

            <v-list-item append-icon="mdi-poll" class="mt-10 mb-10" @click="openPlotDialog('histogram')">Histogram</v-list-item>
            <v-list-item append-icon="mdi-chart-line" class="mt-10 mb-10" @click="openDialogComponent('LogPlotDialog')">LogPlot</v-list-item>

   
      

        
            
          </v-list>
        
            <v-container class="position-absolute bottom-0 d-flex flex-column justify-center">
                <v-btn
                  @click="openDialogComponent('ConfirmDeleteAccountDialog')" 
                  elevation="0" 
                  append-icon="mdi-delete" 
                  class="mb-5 delete-account text-center"
                >
                  Delete Account
                </v-btn>
                <v-btn elevation="0" append-icon="mdi-logout" @click="authStore.logout">Logout</v-btn>
            </v-container>
        


        </v-navigation-drawer>
  
        
</template>

<style scoped>


.delete-account {
   color: red
}

</style>