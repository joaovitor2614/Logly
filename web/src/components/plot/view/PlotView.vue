<script setup lang="ts">

import { PlotType  } from '../types';
import { watch, ref } from 'vue';
import { PlotProvider, PLOT_DIV_ID_BY_PLOT_TYPE } from './provider/plotprovider';
import { getWellLogDataByID } from '@/utils/well';

interface Props {
    plotType: `${PlotType}`,
    template: App.Plot.Template
}

const props = defineProps<Props>();
const plotDivID = ref(PLOT_DIV_ID_BY_PLOT_TYPE[props.plotType])



const populatePlotData = async () => {
    props.template.axes.x.data = await getWellLogDataByID(props.template.axes.x.id, props.template.wellID)
    if (props.template.type === 'histogram') return
    props.template.axes.y.data = await getWellLogDataByID(props.template.axes.y.id, props.template.wellID)
}

const plot = () => {

    const plotProvider = new PlotProvider(props.template)
    plotProvider.run()

}

watch(() => props.template.hasTemplateChanged, async () => {

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