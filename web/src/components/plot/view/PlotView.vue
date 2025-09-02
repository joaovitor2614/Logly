<script setup lang="ts">

import { usePlotStore, useWellStore } from '@/stores';
import { PlotType } from '../types';
import { watch, ref } from 'vue';
import { getWellLogDataByIDs } from '@/api/services/well';
import { PlotProvider, PLOT_DIV_ID_BY_PLOT_TYPE } from './plotprovider';

interface Props {
    plotType: `${PlotType}`,
}

const props = defineProps<Props>();
const plotDivID = ref(PLOT_DIV_ID_BY_PLOT_TYPE[props.plotType])

const plotStore = usePlotStore()
const wellStore = useWellStore()

const template = props.plotType === 'histogram' ? plotStore.histogramTemplate : plotStore.crossPlotTemplate;

const parseWellLogDataIntoValidJsArray = (stringfiedData: string) => {

    const cleaned = stringfiedData.replace(/^"|"$/g, "");
    
    const arr = cleaned
    .split(",")                // break into pieces
    .map(s => s.trim())        // remove spaces
    .map(s => s === "NaN" ? NaN : parseFloat(s)); // convert numbers, keep NaN
    
    return arr

}   

const fetchWellLogData =  async () => {
    const xWellLogData = await getAxisWellLogData(template.xWellLogID)
    let yWellLogData = []
    if (props.plotType === 'scatter') {
         yWellLogData = await getAxisWellLogData(template.yWellLogID)
    }
    const plotData = prepareWellLogData(xWellLogData, yWellLogData)
    plotWellLogData(plotData)
}

const prepareWellLogData = (xWellLogData: Array<Number>, yWellLogData: Array<Number>) => {
    return {
        x: xWellLogData,
        y: yWellLogData
    }
}

const plotWellLogData = (plotData: Record<string, Array<Number>>) => {
    const wellInfo = wellStore.wells.find(well => well._id === template.wellID)
    const xWellLogName = wellInfo?.welllogs.find(wellLog => wellLog._id === template.xWellLogID)?.name
    const yWellLogName = props.plotType === 'scatter' ? wellInfo?.welllogs.find(wellLog => wellLog._id === template.yWellLogID)?.name : ''
    console.log('names', xWellLogName, yWellLogName)
    const plotProvider = new PlotProvider(props.plotType, plotData, xWellLogName, yWellLogName)
    plotProvider.run()
;
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
    console.log('WACH FIRED')
    fetchWellLogData()
})



</script>

<template>
    <div :id="plotDivID">
    
    </div>
</template>

<style scoped>

</style>