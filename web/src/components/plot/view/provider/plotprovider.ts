import Plotly from 'plotly.js-dist';

import { initializePlotLayout, initializePlotTrace } from './utils';



export const PLOT_DIV_ID_BY_PLOT_TYPE = {
    histogram: 'histogramPlot',
    scatter: 'crossplotPlot'
}





export class PlotProvider {
    plotInfo: App.Plot.Template;

    constructor(plotInfo: App.Plot.Template) {
        this.plotInfo = plotInfo;

    }

    run() {
        let layout = initializePlotLayout()
        let plotTrace = initializePlotTrace()
        plotTrace.marker = {
            color: this.plotInfo.color
        }
        console.log('this.plotInfo.axes', this.plotInfo.axes)
        layout.xaxis.title.text = this.plotInfo.axes.x.name
        layout.xaxis.range = this.plotInfo.axes.x.range      
        plotTrace.x = this.plotInfo.axes.x.data
        console.log('this.plotInfo', this.plotInfo)
    
        if (this.plotInfo.type === 'histogram')  {
            plotTrace.type = 'histogram'

        } else {
            if (!this.plotInfo.axes.y.data.length) {
                throw "No y data for crossplot"
            }
            plotTrace.y = this.plotInfo.axes.y.data
            plotTrace.mode = 'markers';
            plotTrace.type = 'scatter';
            layout.yaxis = {
                title: {
                    text: this.plotInfo.axes.y.name
                },
                range:  this.plotInfo.axes.y.range
            }

        }
        console.log('final mainPlotTrace', plotTrace)
        const plotData = [plotTrace]
        console.log('plotData', plotData, 'layout', layout)
        Plotly.newPlot(PLOT_DIV_ID_BY_PLOT_TYPE[this.plotInfo.type], plotData, layout)

    }
}