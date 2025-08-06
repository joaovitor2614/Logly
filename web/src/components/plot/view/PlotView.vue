<script setup lang="ts">
import { Ref, ref } from 'vue'
import { usePlotStore } from '@/stores';
//import Chart from 'chart.js/auto';
import { onMounted } from 'vue';
import { getWellLogDataByIDs } from '@/api/services/well';
const plotStore = usePlotStore()

const isDataLoaded: Ref<boolean> = ref(false)

const setWellLogData = async () => {
    
    const response = await getWellLogDataByIDs(plotStore.wellID, plotStore.xAxisSelectedWellLog)
    const response2 = await getWellLogDataByIDs(plotStore.wellID, plotStore.yAxisSelectedWellLog)
}

onMounted(async () => {
    //await setWellLogData()
    //isDataLoaded.value = true
})
</script>

<template>
    <div id="plotDiv">
    
    </div>
</template>

<style scoped>

</style>