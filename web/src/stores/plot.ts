import { PlotType } from '@/components/plot/types'
import { getNewPlotTemplate } from '@/utils/getNewPloTemplate'
import { defineStore } from 'pinia'
import { ref, type Ref } from 'vue'



export const usePlotStore = defineStore('plotStore', () => {
    const crossPlotTemplate: Ref<App.Plot.Template> = ref(getNewPlotTemplate('histogram'))
    const histogramTemplate: Ref<App.Plot.Template> = ref(getNewPlotTemplate('scatter'))
    


    const plotTemplateByType: Record<PlotType, Ref<App.Plot.Template>> = {
        'histogram': histogramTemplate,
        'scatter': crossPlotTemplate
    }

    const registerPlot = (plotTeplate: App.Plot.Template, plotType: `${PlotType}`) => {
        const template = plotTemplateByType[plotType]
        template.value.wellID = plotTeplate.wellID
        template.value.axes.x.id = plotTeplate.axes.x.id
        if (plotType === 'scatter') {
            template.value.axes.y.id = plotTeplate.axes.y.id
        }
        template.value.hasTemplateChanged = !template.value.hasTemplateChanged

        
    }


    return ({
        histogramTemplate,
        crossPlotTemplate,
        registerPlot
    })

})