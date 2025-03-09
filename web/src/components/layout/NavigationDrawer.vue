<script setup lang="ts">
import { useAuthStore } from '../../stores/index';
import { router } from '../../router/router'
const authStore = useAuthStore();
</script>

<template>
        <v-navigation-drawer
          theme="dark"
          permanent
          rail
        >
          <v-list-item
            prepend-avatar="https://randomuser.me/api/portraits/women/75.jpg"
            nav
          ></v-list-item>
  
          <v-divider></v-divider>
  
          <v-list
            density="compact"
            nav
          >
            <v-list-item prepend-icon="mdi-view-dashboard" value="dashboard"></v-list-item>
  
            <v-list-item prepend-icon="mdi-forum" value="messages"></v-list-item>
          </v-list>
        </v-navigation-drawer>
  
        <v-navigation-drawer permanent>
          <v-list>
            <v-list-item @click="router.push('/')">Home</v-list-item>
            <v-list-item @click="router.push('/profile')">Edit Profile</v-list-item>

            
            <v-btn @click="authStore.logout">Logout</v-btn>
   
           
          </v-list>
        </v-navigation-drawer>
</template>

<style scoped>

</style>