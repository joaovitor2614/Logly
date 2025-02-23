import { defineStore } from 'pinia'

interface dialogWindow {
    name: string,
    props: string[]
}
interface dialogState {
    shouldOpenDialog: boolean,
    dialogWindow: {} | dialogWindow
}


export const useDialogStore = defineStore('dialogStore', {
  state: (): dialogState => ({
    shouldOpenDialog: false,
    dialogWindow: {}
  }),
  actions: {
    openDialogWindow(dialogWindowName : string, dialogWindowProps = undefined) {

      this.dialogWindow = {
        name: dialogWindowName,
        props: dialogWindowProps
      }
      this.shouldOpenDialog = true;
    },
    closeDialogWindow() {
      this.shouldOpenDialog = false // Close all active windows
      this.dialogWindow = {}
    }
  }
})