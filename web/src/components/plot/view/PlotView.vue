<script setup lang="ts">

import { usePlotStore } from '@/stores';
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
    if (props.plotType === 'crossplot') {
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
    const plotProvider = new PlotProvider(props.plotType, plotData)
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