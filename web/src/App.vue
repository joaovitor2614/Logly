<script setup lang="ts">
import { onBeforeMount } from 'vue'
import { deleteAPIHeadersAuthToken, setAPIHeadersBearerToken } from './api/utils'
import { useAuthStore, useUserStore } from './stores/index';
import { router } from './router/router'
import { watch } from 'vue';

const authStore = useAuthStore();
const userStore = useUserStore()

onBeforeMount(() => {
  
  const token = localStorage.getItem('token')
  if (token) {
    
    setAPIHeadersBearerToken(token)
    authStore.token = token
    userStore.getUserInfo()
    authStore.isAuthenticated = true
    router.push('/')
  }
})



</script>

<template>
    <div>
      <v-app>
        <v-main>
          <router-view :key="$route.fullPath" />
        </v-main>
      </v-app>
    </div>
</template>

<style scoped>

</style>
