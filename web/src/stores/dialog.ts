import { defineStore } from "pinia"
import { ref, Ref } from "vue"



export const useDialogStore = defineStore('dialogStore', () => {
    const shouldOpenDialog: Ref<boolean> = ref(false)
    const dialogName: Ref<string> = ref('')
    const dialogProps: Ref<Record<string, any>> = ref({})

    const openDialogWindow = (name: string, props: Record<string, any> = {}) => {
        shouldOpenDialog.value = true
        dialogName.value = name
        dialogProps.value = props
    }

    const closeDialogWindow = () => {
        shouldOpenDialog.value = false
        dialogName.value = ''
    }

    return { 
        shouldOpenDialog,
        openDialogWindow,
        closeDialogWindow,
        dialogName,
        dialogProps
    }
})