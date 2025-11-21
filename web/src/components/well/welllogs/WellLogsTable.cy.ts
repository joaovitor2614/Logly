import { useWellStore } from "@/stores";
import WellLogsTable from "./WellLogsTable.vue";
import { wellsDummyInfo, wellLogsDummyInfo } from '@/test/utils/redirect'




describe('<WellLogsTable />', () => {
    it('renders', () => {
        cy.mountWithPiniaVuetify(WellLogsTable, {
            props: {
                wellLogsInfo: wellLogsDummyInfo,
    
                }
        })
        //const wellStore = useWellStore()


        const expectedRowsAmount = wellLogsDummyInfo.length

        cy.get('#test-well-logs-table tbody tr').should('have.length', expectedRowsAmount);

        //cy.then(() => wellStore.wells.pop())

        //cy.get('#test-well-logs-table tbody tr').should('have.length', expectedRowsAmount-1);
    
    })
  

})