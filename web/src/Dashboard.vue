<script setup lang="ts">
import UtilitiesDrawer from '@/components/drawer/UtilitiesDrawer.vue';
import WellImport from '@/components/well/WellImport.vue';
import { useDialogStore } from './stores';


defineOptions({
    name: 'Dashboard'
})

const dialogStore = useDialogStore()

</script>

<template>
    <v-container fluid style="max-width: 125vh;">
       <UtilitiesDrawer />
        <component :is="dialogStore.dialogName"></component>
       <h1>Dashboard</h1>
       <WellImport />
    </v-container>
 </template>

<style scoped>

</style>