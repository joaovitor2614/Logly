import { PlotType } from '@/components/plot/types'
import { defineStore } from 'pinia'
import { ref, type Ref } from 'vue'



export const usePlotStore = defineStore('plotStore', () => {
    const histogramTemplate: Ref<App.Plot.Template | undefined> = ref(undefined)
    const crossPlotTemplate: Ref<App.Plot.Template | undefined> = ref(undefined)

    


    const plotTemplateByType: Record<PlotType, Ref<App.Plot.Template>> = {
        'histogram': histogramTemplate,
        'scatter': crossPlotTemplate
    }

    const registerPlot = (plotTemplate: App.Plot.Template, plotType: `${PlotType}`) => {
        plotTemplateByType[plotType].value = plotTemplate

        plotTemplateByType[plotType].value.hasTemplateChanged = !plotTemplateByType[plotType].value.hasTemplateChanged
        console.log('plotTemplateByType[plotType]', plotTemplateByType[plotType].value)
        
    }


    return ({
        histogramTemplate,
        crossPlotTemplate,
        registerPlot
    })

})