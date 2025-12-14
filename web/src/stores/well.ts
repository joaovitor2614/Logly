import { getAllWellsData, importWellFile, deleteWellByID, deleteWellLogByIDS } from "@/api/services/well"
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

    const importNewFile = async (lasFile: File) => {
        const response = await importWellFile(lasFile)
        console.log('store import well response', response)
        if (response) {
            toast.success(`Well imported successfully!`)
            getWells()
        }
        return response
    }

    const deleteWell = async (wellID: string) => {
        const response = await deleteWellByID(wellID)
        if (!response) return
      
        wells.value = wells.value.filter(well => well._id !== wellID)
        
    }

    const deleteWellLog = async (wellID: string, wellLogID: string) => {
        const response = await deleteWellLogByIDS(wellLogID, wellID)
        if (!response) return
   
            
        let wellInfo = wells.value.find(well => well._id === wellID)
  
        if (!wellInfo) return
        wellInfo.welllogs = wellInfo.welllogs.filter(wellLog => wellLog._id !== wellLogID)

        
    }
    return { 
        wells,
        deleteWell,
        importNewFile,
        deleteWellLog,
        getWells
    }
})