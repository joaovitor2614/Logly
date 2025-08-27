import Plotly from 'plotly.js-dist';
import { PlotType } from '../types';

export class PlotProvider {
    plotType: string;
    plotData: Record<string, Array<Number>>
    constructor(plotType: `${PlotType}`, plotData: Record<string, Array<Number>>) {
        this.plotType = plotType;
        this.plotData = plotData
    }

    run() {
        console.log('RUNNN')
        if (this.plotType === 'histogram')  {
            const trace = {
                x: this.plotData.x,
                type: 'histogram',
            }
            const plotData = [trace]

            Plotly.newPlot('plotDiv', plotData)
        } else {
            console.log('here scatepper')
            if (!this.plotData.y.length) {
                throw "No y data for crossplot"
            }
            const trace1 = {
                x: this.plotData.x,
                y: this.plotData.y,
                mode: 'markers',
                type: 'scatter'
            };
            Plotly.newPlot('plotDiv', trace1)
       
        }

       
    }
}