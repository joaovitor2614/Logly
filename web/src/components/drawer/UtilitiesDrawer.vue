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
          <div class="d-flex flex-column  drawer-btns-box">
            <v-btn 
              @click="openDialogComponent('ConfirmDeleteAccountDialog')" 
              elevation="0" 
              append-icon="mdi-delete" 
              class="mb-5 delete-account"
            >
              Delete account
            </v-btn>
            <v-btn elevation="0" append-icon="mdi-logout" @click="authStore.logout">Logout</v-btn>
          </div>

        </v-navigation-drawer>
  
        
</template>

<style scoped>
.drawer-btns-box {
  margin-top: 18vh;
}

.delete-account {
   color: red
}

</style>