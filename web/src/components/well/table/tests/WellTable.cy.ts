import { useWellStore } from '@/stores'
import WellTable from '../WellTable.vue'
import { wellsDummyInfo } from './data'



describe('<WellTable />', () => {
    it('renders', () => {
    cy.mountWithPiniaVuetify(WellTable)
      const wellStore = useWellStore()
      wellStore.wells = wellsDummyInfo

      const expectedRowsAmount = wellsDummyInfo.length

      cy.get('#test-well-table tbody tr').should('have.length', expectedRowsAmount);
   
    })
  

})