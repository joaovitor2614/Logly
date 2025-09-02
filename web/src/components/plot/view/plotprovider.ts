import Plotly from 'plotly.js-dist';
import { PlotType } from '../types';



export const PLOT_DIV_ID_BY_PLOT_TYPE = {
    histogram: 'histogramPlot',
    scatter: 'crossplotPlot'
}

export class PlotProvider {
    plotType: string;
    plotData: Record<string, Array<Number>>
    xWellLogName: string
    yWellLogName: string
    constructor(plotType: `${PlotType}`, plotData: Record<string, Array<Number>>, xWellLogName: string = '', yWellLogName: string = '') {
        this.plotType = plotType;
        this.plotData = plotData;
        this.xWellLogName = xWellLogName;
        this.yWellLogName = yWellLogName
    }

    run() {
        let layout = {
            xaxis: {
                title: {
                    text: this.xWellLogName
                }
            }
        }
        let mainPlotTrace = {
            x: this.plotData.x,
        }
        console.log('inicial mainPlotTrace type', mainPlotTrace, this.plotType)
        if (this.plotType === 'histogram')  {
            mainPlotTrace.type = 'histogram'

        } else {
            if (!this.plotData.y.length) {
                throw "No y data for crossplot"
            }
            mainPlotTrace.y = this.plotData.y;
            mainPlotTrace.mode = 'markers';
            mainPlotTrace.type = 'scatter';
            layout.yaxis = {
                title: {
                    text: this.yWellLogName
                }
            }

        }
        console.log('final mainPlotTrace', mainPlotTrace)
        const plotData = [mainPlotTrace]
        Plotly.newPlot(PLOT_DIV_ID_BY_PLOT_TYPE[this.plotType], plotData, layout)

    }
}