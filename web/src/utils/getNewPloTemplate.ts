

export function getNewPlotTemplate() {
    return {
        wellID: '',
        axes: {
            x: {
                id: '',
                range: []
            },
            y: {
                id: '',
                range: []
            }
        },
        hasTemplateChanged: false
    }
}
