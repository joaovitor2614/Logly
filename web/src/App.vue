<script setup lang="ts">
import { onBeforeMount } from 'vue'
import { deleteAPIHeadersAuthToken, setAPIHeadersBearerToken } from './api/utils'

onBeforeMount(() => {

  // Inseri token de autenticação prévia no headers do API

  if (localStorage.token) {
    setAPIHeadersBearerToken(localStorage.token)
  }
  window.addEventListener('storage', () => {
    console.log('called when token set', localStorage.token)
    if (!localStorage.token) {
      deleteAPIHeadersAuthToken()
    } else {
      setAPIHeadersBearerToken(localStorage.token)
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
