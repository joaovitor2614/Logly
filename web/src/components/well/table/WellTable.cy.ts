import { useWellStore } from '@/stores'
import WellTable from './WellTable.vue'



describe('<WellTable />', () => {
    it('renders', () => {
    cy.mountWithPiniaVuetify(WellTable)
      const wellStore = useWellStore()
      wellStore.wells = [
    {
        name: 'Well 1',
        create_time: '2022-01-01T00:00:00.000Z',
        welllogs: []
      },
      {
        name: 'Well 2',
        create_time: '2022-01-01T00:00:00.000Z',
        welllogs: []
      },
    ]

    cy.get('#test-well-table tbody tr').should('have.length', 2);
   
    })
  

})