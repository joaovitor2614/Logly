

export function getNewPlotTemplate(): App.Plot.Template {
    return {
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
