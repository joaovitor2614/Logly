import { defineStore } from 'pinia'
import { ref, type Ref } from 'vue'



export const usePlotStore = defineStore('plotStore', () => {
    const xAxisSelectedWellLog: Ref<string> = ref('');
    const yAxisSelectedWellLog: Ref<string> = ref('');
    const wellID: Ref<string> = ref('');

    const registerPlot = (xAxisLogID: string, yAxisLogID: string, selectedWellID: string) => {
        xAxisSelectedWellLog.value = xAxisLogID;
        yAxisSelectedWellLog.value = yAxisLogID;
        wellID.value = selectedWellID
    }


    return ({
        xAxisSelectedWellLog,
        yAxisSelectedWellLog,
        wellID,
        registerPlot
    })

})