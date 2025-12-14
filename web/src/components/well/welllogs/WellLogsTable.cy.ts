import { useWellStore } from "@/stores";
import WellLogsTable from "./WellLogsTable.vue";
import { wellsDummyInfo, wellLogsDummyInfo } from '@/test/utils/redirect'
import { mount, flushPromises } from '@vue/test-utils'
import axios from 'axios'



describe('<WellLogsTable />', () => {
    it('renders', () => {
        cy.stub(axios, 'post')
        .resolves({ data: { success: true } }) 
        cy.mountWithPiniaVuetify(WellLogsTable, {
            props: {
                wellLogsInfo: wellLogsDummyInfo,
    
                }
        })
        //const wellStore = useWellStore()


        const expectedRowsAmount = wellLogsDummyInfo.length

        cy.get('#test-well-logs-table tbody tr').should('have.length', expectedRowsAmount);

        cy.get('[data-test="delete-btn-jajsojsajosa"]').click()

        cy.get('#test-well-logs-table tbody tr').should('have.length', expectedRowsAmount-1);

        //cy.then(() => wellStore.wells.pop())

        //cy.get('#test-well-logs-table tbody tr').should('have.length', expectedRowsAmount-1);
    
    })
  

})