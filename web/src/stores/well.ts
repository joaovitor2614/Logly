import { getAllWellsData, importWellFile } from "@/api/services/well"
import { defineStore } from "pinia"
import { ref, Ref } from "vue"



export const useWellStore = defineStore('wellStore', () => {
    const wells: Ref<App.Well.Well[]> = ref([])


    const getWells = async () => {
        const response = await getAllWellsData();
        if (response) {
           
            wells.value = response.data
        }
    }

    const importNewFile = async (lasFilePath: string, wellName: string) => {
        const response = await importWellFile(lasFilePath, wellName
            
        )
        if (response) {
            getWells()
        }
    }
    return { 
        wells,
        importNewFile,
        getWells
    }
})