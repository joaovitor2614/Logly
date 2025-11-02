import { PlotType } from '@/components/plot/types'
import { getNewPlotTemplate } from '@/utils/getNewPloTemplate'
import { defineStore } from 'pinia'
import { ref, type Ref } from 'vue'
interface AxisTemplate {
    id: string,
    range: [Number, Number]
}
interface Axes {
    x: AxisTemplate,
    y: AxisTemplate
}
interface PlotTemplate {
    wellID: string,
    axes: Axes,
    hasTemplateChanged: boolean
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