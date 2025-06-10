import { defineStore } from "pinia"
import { ref, Ref } from "vue"



export const useDialogStore = defineStore('dialogStore', () => {
    const shouldOpenDialog: Ref<boolean> = ref(false)
    const dialogName: Ref<string> = ref('')

    return { 
        shouldOpenDialog,
        dialogName
    }
})