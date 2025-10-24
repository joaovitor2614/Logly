<script setup lang="ts">
import {computed, onBeforeMount, ref, Ref} from 'vue'
import { getParsedWellLogByID } from '@/utils/well';
import { useRoute, useRouter } from 'vue-router';
import { useWellStore } from '@/stores';

const wellStore = useWellStore()

const isLoading: Ref<boolean> = ref(false)
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
const router = useRouter()
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

const returnToDashboard = () => {
    router.push("/dashboard")
}

onBeforeMount(async () => {
    isLoading.value = true
    setWellLogInfo();
    await setWellLogDataToDisplay()
    isLoading.value = false;
})
</script>

<template>
    <v-container class="d-flex flex-column justify-center">
        <div class="d-flex justify-start">
             <v-btn
                    icon
                    @click="returnToDashboard()"
                    variant="text"
                    style="color: black"
                    
                >
                    <v-icon >mdi-arrow-left</v-icon>
            </v-btn>
        </div>
    </v-container>
    <v-container class="d-flex flex-column justify-center">
                <v-data-table
                    class="mt-2 mb-10"
                    :headers="wellLogDataTableHeaders"
                    :items="wellLogDataTableItems"
                    :loading="isLoading"
                    :id="'test-well-table'"
                    disable-pagination
                    :items-per-page="-1"
                    hide-default-footer
                 
                  
                >
            
                </v-data-table>
    </v-container>
</template>

<style scoped>

</style>