

export function getNewPlotTemplate(type: 'histogram' | 'scatter'): App.Plot.Template {
    return {
        type,
        wellID: '',
        color: '#0000FF',
        axes: {
            x: {
                id: '',
                name: '',
                range: [],
                data: [],
                unit: ''
            },
            y: {
                id: '',
                name: '',
                range: [],
                data: [],
                unit: ''
            }
        },
        hasTemplateChanged: false
    }
}
