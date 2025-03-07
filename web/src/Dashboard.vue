<script setup lang="ts">
import ProfessorGalery from './components/main/ProfessorGalery.vue'
import NavigationDrawer from './components/layout/NavigationDrawer.vue'
import ProfessorActions from './components/main/ProfessorActions.vue'
defineOptions({
    name: 'Dashboard'
})
console.log('hashihsaas')

</script>

<template>
    <NavigationDrawer />
    <ProfessorActions />
    <ProfessorGalery />
 </template>

<style scoped>

</style>