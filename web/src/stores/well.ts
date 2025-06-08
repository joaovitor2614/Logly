import { defineStore } from "pinia"
import { ref, Ref } from "vue"



export const useWellStore = defineStore('wellStore', () => {
    const wells: Ref<App.Well.Well[]> = ref([])

    return { 
        wells,
    }
})