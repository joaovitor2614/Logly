<script setup lang="ts">
import ProfessorGalery from './components/professor/ProfessorGalery.vue'
import ProfessorActions from './components/professor/ProfessorActions.vue'
defineOptions({
    name: 'Dashboard'
})
console.log('hashihsaas')

</script>

<template>
    <v-container fluid style="max-width: 125vh;">

    
        <ProfessorActions />
        <ProfessorGalery />
    </v-container>
 </template>

<style scoped>

</style>