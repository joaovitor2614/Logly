import Plotly from 'plotly.js-dist';

import { initializePlotLayout, initializePlotTrace } from './utils';



export const PLOT_DIV_ID_BY_PLOT_TYPE = {
    histogram: 'histogramPlot',
    scatter: 'crossplotPlot'
}





export class PlotProvider {
    plotInfo: App.Plot.Template;
    layout: Partial<Plotly.Layout>;
    plotTrace: Partial<Plotly.PlotData>;

    constructor(plotInfo: App.Plot.Template) {
        this.plotInfo = plotInfo;
        this.layout = initializePlotLayout()
        this.plotTrace

    }
    initializePlotlyElements() {
        this.layout = initializePlotLayout()
        this.plotTrace = initializePlotTrace()
    }
    setPopulatePlotTraceConfig() {
        this.plotTrace.marker = {
            color: this.plotInfo.color
        }
        this.layout.xaxis.title.text = this.plotInfo.axes.x.name
        this.layout.xaxis.range = this.plotInfo.axes.x.range      
        this.plotTrace.x = this.plotInfo.axes.x.data
    }

    renderPlot() {
        
        const plotData = [this.plotTrace]
        console.log('plotData', plotData, 'layout', this.layout)
        Plotly.newPlot(PLOT_DIV_ID_BY_PLOT_TYPE[this.plotInfo.type], plotData, this.layout)
    }

    setSpecificPlotTypeConfig() {
        if (this.plotInfo.type === 'histogram')  {
            this.plotTrace.type = 'histogram'

        } else {
            if (!this.plotInfo.axes.y.data.length) {
                throw "No y data for crossplot"
            }
            this.plotTrace.y = this.plotInfo.axes.y.data
            this.plotTrace.mode = 'markers';
            this.plotTrace.type = 'scatter';
            this.layout.yaxis = {
                title: {
                    text: this.plotInfo.axes.y.name
                },
                range:  this.plotInfo.axes.y.range
            }

        }
    }
    run() {
        this.initializePlotlyElements();
        this.setPopulatePlotTraceConfig()
        this.setSpecificPlotTypeConfig()
 
        
     
    

        this.renderPlot()


    }
}