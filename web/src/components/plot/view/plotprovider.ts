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
        const trace = {
        x: this.plotData.x,
        type: 'histogram',
    }
    const plotData = [trace]

    Plotly.newPlot('plotDiv', plotData)
       
    }
}