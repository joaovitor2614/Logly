<script setup lang="ts">
import ProfessorGalery from './components/professor/ProfessorGalery.vue'
import ProfessorSearchFilters from './components/professor/ProfessorSearchFilters.vue'

import AddProfessorDialog from './components/professor/actions/AddProfessorDialog.vue'

defineOptions({
    name: 'Dashboard'
})



</script>

<template>
    <v-container fluid style="max-width: 125vh;">

        <AddProfessorDialog />
        <ProfessorSearchFilters />
        <ProfessorGalery />
    </v-container>
 </template>

<style scoped>

</style>