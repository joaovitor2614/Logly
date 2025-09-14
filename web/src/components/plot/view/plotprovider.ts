import Plotly from 'plotly.js-dist';
import { PlotInfo } from '../types';



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
        let layout = {
            xaxis: {
                title: {
                    text: this.plotInfo.x.name
                }
            }
        }
        let mainPlotTrace = {
            x: this.plotInfo.x.data,
        }
    
        if (this.plotInfo.type === 'histogram')  {
            mainPlotTrace.type = 'histogram'

        } else {
            if (!this.plotInfo.y.data.length) {
                throw "No y data for crossplot"
            }
            mainPlotTrace.y = this.plotInfo.y.data
            mainPlotTrace.mode = 'markers';
            mainPlotTrace.type = 'scatter';
            layout.yaxis = {
                title: {
                    text: this.plotInfo.y.name
                }
            }

        }
        console.log('final mainPlotTrace', mainPlotTrace)
        const plotData = [mainPlotTrace]
        Plotly.newPlot(PLOT_DIV_ID_BY_PLOT_TYPE[this.plotInfo.type], plotData, layout)

    }
}