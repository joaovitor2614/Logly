<script setup lang="ts">
import ProfessorGalery from './components/professor/ProfessorGalery.vue'
import ProfessorActions from './components/professor/ProfessorActions.vue'
defineOptions({
    name: 'Dashboard'
})
console.log('hashihsaas')

</script>

<template>
    <ProfessorActions />
    <ProfessorGalery />
 </template>

<style scoped>

</style>