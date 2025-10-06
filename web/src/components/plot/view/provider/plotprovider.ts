import Plotly from 'plotly.js-dist';
import { PlotInfo } from '../../types';
import { initializePlotLayout, initializePlotTrace } from './utils';



export const PLOT_DIV_ID_BY_PLOT_TYPE = {
    histogram: 'histogramPlot',
    scatter: 'crossplotPlot'
}





export class PlotProvider {
    plotInfo: PlotInfo;

    constructor(plotInfo: PlotInfo) {
        this.plotInfo = plotInfo;

    }

    run() {
        let layout = initializePlotLayout()
        let plotTrace = initializePlotTrace()
        layout.xaxis.title.text = this.plotInfo.x.name
        plotTrace.x = this.plotInfo.x.data

    
        if (this.plotInfo.type === 'histogram')  {
            plotTrace.type = 'histogram'

        } else {
            if (!this.plotInfo.y.data.length) {
                throw "No y data for crossplot"
            }
            plotTrace.y = this.plotInfo.y.data
            plotTrace.mode = 'markers';
            plotTrace.type = 'scatter';
            layout.yaxis = {
                title: {
                    text: this.plotInfo.y.name
                }
            }

        }
        console.log('final mainPlotTrace', plotTrace)
        const plotData = [plotTrace]
        Plotly.newPlot(PLOT_DIV_ID_BY_PLOT_TYPE[this.plotInfo.type], plotData, layout)

    }
}