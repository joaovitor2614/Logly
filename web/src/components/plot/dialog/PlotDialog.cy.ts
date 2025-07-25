import { useDialogStore, useWellStore } from '@/stores'
import PlotDialog from './PlotDialog.vue'



describe('<PlotDialog />', () => {
    it('renders when dialog store is open', () => {
    cy.mountWithPiniaVuetify(PlotDialog)
      const dialogStore = useDialogStore()
      dialogStore.shouldOpenDialog = true

      cy.get("#test-selected-wells-to-plot-selector").should('exist')
      cy.get("#test-plot-dialog-btn").should('exist')




    })
    it('does not renders when dialog store is not open', () => {
    cy.mountWithPiniaVuetify(PlotDialog)


      cy.get("#test-selected-wells-to-plot-selector").should('not.exist')
      cy.get("#test-plot-dialog-btn").should('not.exist')


    })
  

})