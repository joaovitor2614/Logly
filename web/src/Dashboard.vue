<script setup lang="ts">
import WellImport from './components/well/WellImport.vue';


defineOptions({
    name: 'Dashboard'
})



</script>

<template>
    <v-container fluid style="max-width: 125vh;">

       <h1>Dashboard</h1>
       <WellImport />
    </v-container>
 </template>

<style scoped>

</style>