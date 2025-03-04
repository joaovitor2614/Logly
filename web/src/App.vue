<script setup lang="ts">
import { onBeforeMount } from 'vue'
import { deleteAPIHeadersAuthToken, setAPIHeadersBearerToken } from './api/utils'
import { useAuthStore, useUserStore } from './stores/index';
import { router } from './router/router'
onBeforeMount(() => {
  const authStore = useAuthStore();
  const token = localStorage.getItem('token')
  if (token) {
    const userStore = useUserStore()
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
