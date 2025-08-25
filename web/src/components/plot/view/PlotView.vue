<script setup lang="ts">

import { usePlotStore } from '@/stores';
import { PlotType } from '../types';
import { watch } from 'vue';
import { getWellLogDataByIDs } from '@/api/services/well';
//import Plotly from 'plotly.js-dist';
interface Props {
    plotType: `${PlotType}`,
}

const props = defineProps<Props>();

const plotStore = usePlotStore()

const template = props.plotType === 'histogram' ? plotStore.histogramTemplate : plotStore.crossPlotTemplate;

const parseWellLogDataIntoValidJsArray = (stringfiedData: string) => {
    console.log('stringfiedData', stringfiedData)
    const cleaned = stringfiedData.replace(/^"|"$/g, "");
    const dataArray = JSON.parse(cleaned);
    console.log('dataArray', dataArray)
    return dataArray
}

const fetchWellLogData =  async () => {
    const xWellLogData = await getAxisWellLogData(template.xWellLogID)
    if (props.plotType === 'scatter') {
        const yWellLogData = await getAxisWellLogData(template.yWellLogID)
    }
    

}

const getAxisWellLogData = async (wellLogID: string) => {
    const response = await getWellLogDataByIDs(wellLogID, template.wellID)
    if (response) {
        const wellLogData = parseWellLogDataIntoValidJsArray(response.data.data)
        return wellLogData
    } else {
        return []
    }
        
    
}

watch(() => template.wellID, () => {
    fetchWellLogData()
})



</script>

<template>
    <div id="plotDiv">
    
    </div>
</template>

<style scoped>

</style>