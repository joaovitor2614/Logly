import { defineStore } from "pinia"
import { ref, Ref } from "vue"



export const useDialogStore = defineStore('dialogStore', () => {
    const shouldOpenDialog: Ref<boolean> = ref(false)
    const dialogName: Ref<string> = ref('')

    const openDialogWindow = (name: string) => {
        shouldOpenDialog.value = true
        dialogName.value = name
    }

    const closeDialogWidnow = () => {
        shouldOpenDialog.value = false
        dialogName.value = ''
    }

    return { 
        shouldOpenDialog,
        openDialogWindow,
        closeDialogWidnow,
        dialogName
    }
})