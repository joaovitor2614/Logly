<script setup lang="ts">

import { deleteAPIHeadersAuthToken, setAPIHeadersBearerToken } from './api/utils'
import NavigationDrawer from './components/layout/NavigationDrawer.vue';
import { useAuthStore, useProfessorStore, useUserStore } from './stores/index';
import { watch } from 'vue';

const authStore = useAuthStore();
const userStore = useUserStore()
const professorStore = useProfessorStore()

watch(
  () => authStore.token, // Use a getter function to maintain reactivity
  async (token) => {
  console.log('token watch')
  if (token) {

    localStorage.setItem("token", token)
    setAPIHeadersBearerToken(token)
    console.log('here fetch user')
    await userStore.fetchUser()
    await professorStore.fetchProfessorsInfo()
    authStore.isAuthenticated = true;

  } else {
    localStorage.removeItem('token')
    deleteAPIHeadersAuthToken();
    authStore.isAuthenticated = false

  }
},  { immediate: true })






</script>

<template>
    <div>
      <v-app>
        <v-main>
          <NavigationDrawer v-if="authStore.isAuthenticated"/>
          <router-view :key="$route.fullPath" />
        </v-main>
      </v-app>
    </div>
</template>

<style scoped>

</style>
