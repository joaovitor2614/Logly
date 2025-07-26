import { getAllWellsData, importWellFile, deleteWellByID } from "@/api/services/well"
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

    const deleteWell = async (wellID: string) => {
        const response = await deleteWellByID(wellID)
        if (response) {
            wells.value = wells.value.filter(well => well._id !== wellID)
        }
    }
    return { 
        wells,
        deleteWell,
        importNewFile,
        getWells
    }
})