

export function getNewPlotTemplate(type: 'histogram' | 'scatter'): App.Plot.Template {
    return {
        type,
        wellID: '',
        axes: {
            x: {
                id: '',
                range: [],
                data: []
            },
            y: {
                id: '',
                range: [],
                data: []
            }
        },
        hasTemplateChanged: false
    }
}
