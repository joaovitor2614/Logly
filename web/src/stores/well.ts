import { getAllWellsData, importWellFile, deleteWellByID } from "@/api/services/well"
import { defineStore } from "pinia"
import { ref, Ref } from "vue"
import { useToast } from "vue-toastification"

const toast = useToast()

export const useWellStore = defineStore('wellStore', () => {
    const wells: Ref<App.Well.Well[]> = ref([])


    const getWells = async () => {
        const response = await getAllWellsData();
        if (response) {
           
            wells.value = response.data
        }
    }

    const importNewFile = async (lasFilePath: string) => {
        const response = await importWellFile(lasFilePath)
        if (response) {
            toast.success(`Well imported successfully!`)
            getWells()
        }
        return response
    }

    const deleteWell = async (wellID: string) => {
        console.log('wellID', wellID)
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