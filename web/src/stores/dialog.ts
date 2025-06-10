import { defineStore } from "pinia"
import { ref, Ref } from "vue"



export const useDialogStore = defineStore('dialogStore', () => {
    const shouldOpenDialog: Ref<App.Well.Well[]> = ref([])
    const dialogName: Ref<string> = ref('')

    return { 
        shouldOpenDialog,
        dialogName
    }
})