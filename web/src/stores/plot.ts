import { PlotType } from '@/components/plot/types'
import { defineStore } from 'pinia'
import { ref, type Ref } from 'vue'

interface PlotTemplate {
    wellID: string,
    xWellLogID: string,
    yWellLogID: string,
    hasTemplateChanged: boolean
}

function getNewPlotTemplate() {
    return {
        wellID: '',
        xWellLogID: '',
        yWellLogID: '',
        hasTemplateChanged: false
    }
}



export const usePlotStore = defineStore('plotStore', () => {
    const crossPlotTemplate: Ref<PlotTemplate> = ref(getNewPlotTemplate())
    const histogramTemplate: Ref<PlotTemplate> = ref(getNewPlotTemplate())
    


    const plotTemplateByType: Record<PlotType, Ref<PlotTemplate>> = {
        'histogram': histogramTemplate,
        'scatter': crossPlotTemplate
    }

    const registerPlot = (plotTeplate: PlotTemplate, plotType: `${PlotType}`) => {
        const template = plotTemplateByType[plotType]
        template.value.wellID = plotTeplate.wellID
        template.value.xWellLogID = plotTeplate.xWellLogID
        if (plotType === 'scatter') {
            template.value.yWellLogID = plotTeplate.yWellLogID
        }
        template.value.hasTemplateChanged = !template.value.hasTemplateChanged

        
    }


    return ({
        histogramTemplate,
        crossPlotTemplate,
        registerPlot
    })

})