

interface PlotTrace {
    mode: string,
    type: string,
    range: [number, number],
    x: Number[],
    y?: Number[]
}

interface LayoutAxis {
  title: AxisTitle
}

interface AxisTitle {
    text: string
}

interface PlotLayout {
    xaxis: LayoutAxis,
    yaxis: LayoutAxis
}


export const initializePlotLayout = (): PlotLayout => {
    return {
        xaxis: {
                title: {
                    text: ''
                }
        },
        yaxis: {
            title: {
                    text: ''
            }
        }
    }
}

export const initializePlotTrace = (): PlotTrace => {
    return {
        mode: '',
        type: '',
        x: [],
    
    }
}

