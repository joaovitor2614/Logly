<script setup lang="ts">

import { deleteAPIHeadersAuthToken, setAPIHeadersBearerToken } from './api/utils'
import NavigationDrawer from './components/layout/NavigationDrawer.vue';
import { useAuthStore, useProfessorStore, useUserStore } from './stores/index';
import { watch } from 'vue';

const authStore = useAuthStore();
const userStore = useUserStore()
const professorStore = useProfessorStore()

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

    const hasErrors = await userStore.fetchUser()
   
    if (!hasErrors) {
      localStorage.setItem("token", token)
      await professorStore.fetchProfessorsInfo()
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
          <NavigationDrawer v-if="authStore.isAuthenticated"/>
          <router-view :key="$route.fullPath" />
        </v-main>
      </v-app>
    </div>
</template>

<style scoped>

</style>
