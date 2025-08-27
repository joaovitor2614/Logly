import Plotly from 'plotly.js-dist';
import { PlotType } from '../types';
import { h } from 'vue';


export const PLOT_DIV_ID_BY_PLOT_TYPE = {
    histogram: 'histogramPlot',
    crossplot: 'crossplotPlot'
}

export class PlotProvider {
    plotType: string;
    plotData: Record<string, Array<Number>>
    constructor(plotType: `${PlotType}`, plotData: Record<string, Array<Number>>) {
        this.plotType = plotType;
        this.plotData = plotData
    }

    run() {
        let mainPlotTrace = []
    
        if (this.plotType === 'histogram')  {
            mainPlotTrace = {
                x: this.plotData.x,
                type: 'histogram',
            }

        } else {

            if (!this.plotData.y.length) {
                throw "No y data for crossplot"
            }
            mainPlotTrace = {
                x: this.plotData.x,
                y: this.plotData.y,
                mode: 'markers',
                type: 'scatter'
            };
        }

        const plotData = [mainPlotTrace]
        Plotly.newPlot(PLOT_DIV_ID_BY_PLOT_TYPE[this.plotType], plotData)

    }
}