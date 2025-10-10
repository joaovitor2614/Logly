<script setup lang="ts">
import {computed, onBeforeMount, ref, Ref} from 'vue'
import { getParsedWellLogByID } from '@/utils/well';
import { useRoute } from 'vue-router';
import { useWellStore } from '@/stores';

const wellStore = useWellStore()

const currentWellLogInfo: Ref<App.Well.WellLog | undefined> = ref(undefined)

const wellLogDataTableHeaders = computed(() => {
    return [
        {
            title: `${currentWellLogInfo.value?.name} ${currentWellLogInfo.value?.unit}`,
            key: 'data',
            align: 'center'
    }]
})


const route = useRoute()
const currentWellLogData: Ref<Number[]> = ref([])
const wellLogDataTableItems = computed(() => {
    const tableData = []
    console.log('currentWellLogData.value', currentWellLogData.value, typeof currentWellLogData.value[4])
    currentWellLogData.value.forEach((data) => {
        tableData.push({data})
    })
    return tableData
   
})
const setWellLogDataToDisplay = async () => {
    const {well_id, well_log_id } = route.params

 
    currentWellLogData.value = await getParsedWellLogByID(well_log_id as string, well_id as string)
    
}

const setWellLogInfo = () => {
    const selectedWell = wellStore.wells.find(well => well._id === route.params.well_id);
    currentWellLogInfo.value = selectedWell?.welllogs.find(wellLog => wellLog._id === route.params.well_log_id);
    
}

onBeforeMount(async () => {
    setWellLogInfo()
    await setWellLogDataToDisplay()
})
</script>

<template>
    <v-container class="d-flex flex-column justify-center">
                <v-data-table
                    class="mt-2 mb-10"
                    :headers="wellLogDataTableHeaders"
                    :items="wellLogDataTableItems"
                    :id="'test-well-table'"
                 
                    hide-default-footer
                >
            
                </v-data-table>
    </v-container>
</template>

<style scoped>

</style>