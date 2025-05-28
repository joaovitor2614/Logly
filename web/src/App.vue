<script setup lang="ts">

import { deleteAPIHeadersAuthToken, setAPIHeadersBearerToken } from './api/utils'
import { useAuthStore, useUserStore } from './stores/index';
import Header from '@/components/layout/Header.vue'
import { watch } from 'vue';

const authStore = useAuthStore();
const userStore = useUserStore()


const deAuthenticatedUser = () => {
    localStorage.removeItem('token')
    deleteAPIHeadersAuthToken();
    authStore.isAuthenticated = false
}

watch(
  () => authStore.token, // Use a getter function to maintain reactivity
  async (token) => {

  if (token) {


    setAPIHeadersBearerToken(token)

    const response = await userStore.fetchUser()
   
    if (response) {
      localStorage.setItem("token", token)
      authStore.isAuthenticated = true;
    } else {
      deAuthenticatedUser()
    }


  } else {
    deAuthenticatedUser()

  }
},  { immediate: true })






</script>

<template>
    <div>
      <v-app>
        <v-main>
          <Header />
          <router-view :key="$route.fullPath" />
        </v-main>
      </v-app>
    </div>
</template>

<style scoped>

</style>
