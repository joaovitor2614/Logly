<script setup lang="ts">
import ProfessorGalery from './components/professor/ProfessorGalery.vue'
import ProfessorActions from './components/professor/ProfessorActions.vue'
import AddProfessorDialog from './components/professor/actions/AddProfessorDialog.vue'

defineOptions({
    name: 'Dashboard'
})



</script>

<template>
    <v-container fluid style="max-width: 125vh;">

        <AddProfessorDialog />
        <ProfessorActions />
        <ProfessorGalery />
    </v-container>
 </template>

<style scoped>

</style>