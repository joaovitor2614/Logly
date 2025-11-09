<script setup lang="ts">
import PlotEdit from './PlotEdit.vue';
import { usePlotStore, useWellStore } from '@/stores';
import { PlotType, PlotInfo, Axis } from '../types';
import { watch, ref } from 'vue';
import { PlotProvider, PLOT_DIV_ID_BY_PLOT_TYPE } from './provider/plotprovider';
import { getWellLogDataByID } from '@/utils/well';

interface Props {
    plotType: `${PlotType}`,
}

const props = defineProps<Props>();
const plotDivID = ref(PLOT_DIV_ID_BY_PLOT_TYPE[props.plotType])

const plotStore = usePlotStore()
const wellStore = useWellStore()

const template = props.plotType === 'histogram' ? plotStore.histogramTemplate : plotStore.crossPlotTemplate;




const populatePlotData = async (plotInfo: PlotInfo) => {
    plotInfo.x.data = await getWellLogDataByID(template.axes.x.id, template.wellID)
    if (props.plotType === 'histogram') return
    plotInfo.y.data = await getWellLogDataByID(template.axes.y.id, template.wellID)
}

const populateAxisWellLogInfo = (axisWellLogID: string, plotInfoAxis: Axis) => {
    const wellInfo = wellStore.wells.find(well => well._id === template.wellID)
    const wellLogInfo = wellInfo?.welllogs.find(wellLog => wellLog._id === axisWellLogID)
    if (!wellLogInfo) return
    plotInfoAxis.name = wellLogInfo.name;
    plotInfoAxis.unit = wellLogInfo.unit;

}

const populateWellLogInfo = (plotInfo: PlotInfo) => {
    populateAxisWellLogInfo(template.axes.x.id, plotInfo.x)
    populateAxisWellLogInfo(template.axes.y.id, plotInfo.y)
}

const createPlotInfo = async () => {
    let plotInfo = {type: props.plotType, x: {name: '', unit: '', data: []}, y: {name: '', unit: '', data: []}}
    await populatePlotData(plotInfo);
    populateWellLogInfo(plotInfo);
    return plotInfo
}

const plot = (plotInfo: PlotInfo) => {

    const plotProvider = new PlotProvider(plotInfo)
    plotProvider.run()

}

watch(() => template.hasTemplateChanged, async () => {

    const plotInfo = await createPlotInfo()
    plot(plotInfo)
})



</script>

<template>
  
         <div :id="plotDivID">
        </div>

       
  
    
</template>

<style scoped>

</style>