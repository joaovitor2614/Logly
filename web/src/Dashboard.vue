<script setup lang="ts">
import UtilitiesDrawer from '@/components/drawer/UtilitiesDrawer.vue';
import WellImport from '@/components/well/io/import/WellImport.vue';
import { useDialogStore, useWellStore } from './stores';
import { onMounted, ref } from 'vue';
import WellTable from '@/components/well/table/WellTable.vue';
import PlotView from '@/components/plot/view/PlotView.vue';
import PlotSection from '@/components/plot/view/PlotSection.vue';

defineOptions({
    name: 'Dashboard'
})

const dialogStore = useDialogStore()
const wellStore = useWellStore()
const isWellsLoaded = ref(false);

onMounted(async () => {
    await wellStore.getWells();
 
})
</script>

<template>
    <component :is="dialogStore.dialogName" v-bind="dialogStore.dialogProps"></component>
    <v-container>
       <UtilitiesDrawer />
       <WellTable/>
       <PlotSection />
        

 
   
    </v-container>

  

 </template>

<style scoped>

</style>