<script setup lang="ts">
import { onBeforeMount } from 'vue'
import { deleteAPIHeadersAuthToken, setAPIHeadersBearerToken } from './api/utils'
import { useAuthStore } from './stores/auth';





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
