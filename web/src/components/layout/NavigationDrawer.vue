<script setup lang="ts">
import { useAuthStore, useUserStore, useProfessorStore } from '../../stores/index';
import { useRouter } from 'vue-router'

const authStore = useAuthStore();
const userStore = useUserStore()

const router = useRouter()

const professorStore = useProfessorStore()

const openAddProfessorDialog = () => {
  professorStore.shouldOpenAddProfessorDialog = true
}
</script>

<template>

        <v-navigation-drawer
          theme="dark"
          permanent
  
        >
          <v-list-item
            :prepend-avatar="userStore.userInfo.image"
            nav
          ></v-list-item>
          <v-list-item>Welcome {{ userStore.userInfo.name }}</v-list-item>
          <v-divider></v-divider>
  
          <v-list
            density="compact"
            nav
          >
    
            <v-list-item append-icon="mdi-home" class="mt-10 mb-10" @click="router.push('/')">Home</v-list-item>
 
            <v-list-item append-icon="mdi-account" class="mt-10 mb-10" @click="router.push('/profile')">Edit Profile</v-list-item>

            <v-list-item append-icon="mdi-plus" class="mt-10 mb-10" @click="openAddProfessorDialog">Add Professor</v-list-item>
      

        
            
          </v-list>
          <v-btn class="mt-16" @click="authStore.logout">Logout</v-btn>
        </v-navigation-drawer>
  
        
</template>

<style scoped>

</style>