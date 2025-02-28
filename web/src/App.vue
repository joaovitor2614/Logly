<script setup lang="ts">
import { onBeforeMount } from 'vue'
import { deleteAPIHeadersAuthToken, setAPIHeadersAuthToken } from './api/utils'

onBeforeMount(() => {

  // Inseri token de autenticação prévia no headers do API
  if (localStorage.token) {
    setAPIHeadersAuthToken(localStorage.token)
  }
  window.addEventListener('storage', () => {
    if (!localStorage.token) {
      deleteAPIHeadersAuthToken()
    } else {
      setAPIHeadersAuthToken(localStorage.token)
    }
    
  })
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
