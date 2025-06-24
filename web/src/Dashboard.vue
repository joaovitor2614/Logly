<script setup lang="ts">
import UtilitiesDrawer from '@/components/drawer/UtilitiesDrawer.vue';
import WellImport from '@/components/well/import/WellImport.vue';
import { useDialogStore, useWellStore } from './stores';
import { onMounted } from 'vue';
import WellTable from '@/components/well/table/WellTable.vue';


defineOptions({
    name: 'Dashboard'
})

const dialogStore = useDialogStore()
const wellStore = useWellStore()

onMounted(() => {
    wellStore.getWells();
})
</script>

<template>
    <v-container fluid style="max-width: 125vh;">
       <UtilitiesDrawer />
       <WellTable/>
        <component :is="dialogStore.dialogName"></component>
 
   
    </v-container>
 </template>

<style scoped>

</style>