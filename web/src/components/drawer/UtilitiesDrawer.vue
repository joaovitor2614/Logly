<script setup lang="ts">
import { useAuthStore, useUserStore } from '@/stores';



const userStore = useUserStore()
const authStore = useAuthStore()
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
    
            <v-list-item append-icon="mdi-file" class="mt-10 mb-10">Import Well</v-list-item>
 
            <v-list-item append-icon="mdi-chart-scatter-plot" class="mt-10 mb-10">CrossPlot</v-list-item>

            <v-list-item append-icon="mdi-poll" class="mt-10 mb-10">Histogram</v-list-item>
      

        
            
          </v-list>
          <v-btn class="logout-btn" @click="authStore.logout">Logout</v-btn>
        </v-navigation-drawer>
  
        
</template>

<style scoped>

</style>