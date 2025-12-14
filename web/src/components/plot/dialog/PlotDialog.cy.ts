import { useDialogStore, useWellStore } from '@/stores'
import PlotDialog from './PlotDialog.vue'

import { wellsDummyInfo } from '@/test/utils/redirect'
import { verifySelectorItemsAmount } from '@/test/utils/inputs'


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
     it('Selector are correctly populatd', () => {
      cy.mountWithPiniaVuetify(PlotDialog)
      const dialogStore = useDialogStore()
      const wellStore = useWellStore()
      wellStore.wells = wellsDummyInfo
      dialogStore.shouldOpenDialog = true


      verifySelectorItemsAmount('#test-selected-wells-to-plot-selector', wellsDummyInfo.length)

      //verifySelectorItemsAmount('#test-welllog-to-plot-selector', 0)




    })
    
  

})