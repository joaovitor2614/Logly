


export enum PlotType {
    Histogram = 'histogram',
    Scatter = 'scatter',
}

export interface Axis {
    data: Array<Number>,
    name: string,
    unit: string
}

export interface PlotInfo {
    type: string,
    x: Axis,
    y: Axis
}