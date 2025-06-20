<script setup lang="ts">
import { useAuthStore, useDialogStore, useUserStore } from '@/stores';
import { useRouter } from 'vue-router';



const userStore = useUserStore()
const authStore = useAuthStore()
const dialogStore = useDialogStore()
const router = useRouter()
const openDialogComponent = (componentName: string) => {
  dialogStore.openDialogWindow(componentName)
}
</script>

<template>

        <v-navigation-drawer
          theme="dark"
          permanent
         
        >

          <v-list-item>Welcome {{ userStore.userInfo.name }}</v-list-item>
          <v-divider></v-divider>
  
          <v-list
            density="compact"
            nav
          >
            <v-list-item append-icon="mdi-file" class="mt-10 mb-10" @click="router.push('/dashboard')">Dashboard</v-list-item>
            <v-list-item append-icon="mdi-file" class="mt-10 mb-10" @click="openDialogComponent('WellImport')">Import Well</v-list-item>
 
            <v-list-item append-icon="mdi-chart-scatter-plot" class="mt-10 mb-10">CrossPlot</v-list-item>

            <v-list-item append-icon="mdi-poll" class="mt-10 mb-10" @click="openDialogComponent('PlotDialog')">Histogram</v-list-item>
      

        
            
          </v-list>
          <v-btn class="logout-btn" @click="authStore.logout">Logout</v-btn>
        </v-navigation-drawer>
  
        
</template>

<style scoped>

</style>