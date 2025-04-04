<script setup lang="ts">
const props = defineProps({
    /** Vuetify Card Title name */
    helperTitle: {
        type: String,
        required: true
    }
})
</script>

<template>

        <v-container fluid class="d-flex align-center justify-center fill-height">
           
           <v-card elevation="4" class="auth-card">
        
               <v-container>
                   <v-container class="d-flex flex-column align-center justify-center mt-6 mb-6">
                       <h2 class="font-weight-bold mb-4">Welcome to Mamata ou Cilada!</h2>
                       <p class="text-medium-emphasis">{{ props.helperTitle }}</p>
                   </v-container>
                   <slot></slot>
               </v-container>
           </v-card>

       </v-container>
</template>

<style scoped>
.auth-card {
  max-width: 800px;
  width: 100%;
  border-radius: 12px;
  overflow: hidden;
}
</style>