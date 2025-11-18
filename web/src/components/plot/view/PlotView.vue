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




const populatePlotData = async () => {
    template.axes.x.data = await getWellLogDataByID(template.axes.x.id, template.wellID)
    if (props.plotType === 'histogram') return
    template.axes.y.data = await getWellLogDataByID(template.axes.y.id, template.wellID)
}

const plot = () => {

    const plotProvider = new PlotProvider(template)
    plotProvider.run()

}

watch(() => template.hasTemplateChanged, async () => {

    await populatePlotData()
    plot()
})



</script>

<template>
  
         <div :id="plotDivID">
        </div>

       
  
    
</template>

<style scoped>

</style>