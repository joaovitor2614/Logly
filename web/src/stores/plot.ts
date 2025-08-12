import { PlotType } from '@/components/plot/types'
import { defineStore } from 'pinia'
import { ref, type Ref } from 'vue'

interface CrossPlotTemplate {
    wellID: string,
    xWellLogID: string,
    yWellLogID: string
}

interface HistogramTemplate extends Omit<CrossPlotTemplate, 'yWellLogID'>{}

export const usePlotStore = defineStore('plotStore', () => {
    const crossPlotTemplate = ref<CrossPlotTemplate>({
        wellID: '',
        xWellLogID: '',
        yWellLogID: ''
    })
    const histogramTemplate = ref<HistogramTemplate>({
        wellID: '',
        xWellLogID: ''
    })
    
    const xAxisSelectedWellLog: Ref<string> = ref('');
    const yAxisSelectedWellLog: Ref<string> = ref('');
    const wellID: Ref<string> = ref('');

    const plotTemplateByType: Record<PlotType, Ref<CrossPlotTemplate> | Ref<HistogramTemplate>> = {
        'histogram': histogramTemplate,
        'scatter': crossPlotTemplate
    }
    const registerPlot = (plotTeplate: CrossPlotTemplate, plotType: `${PlotType}`) => {
        const template = plotTemplateByType[plotType]
        template.value.wellID = plotTeplate.wellID
        template.value.xWellLogID = plotTeplate.xWellLogID
        
        if (plotType === 'scatter') {
            template.value.yWellLogID = plotTeplate.yWellLogID
        }
    }


    return ({
        xAxisSelectedWellLog,
        yAxisSelectedWellLog,
        wellID,
        registerPlot
    })

})