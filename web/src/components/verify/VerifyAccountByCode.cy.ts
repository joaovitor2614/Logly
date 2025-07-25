import { useDialogStore, useWellStore } from '@/stores'
import VerifyAccountByCode from './VerifyAccountByCode.vue'



describe('<VerifyAccountByCode />', () => {
    it('renders', () => {
    cy.mountWithPiniaVuetify(VerifyAccountByCode)


      cy.get("#test-otp-code-input").should('exist')
      cy.get("#test-verify-otp-btn").should('exist')
      cy.get("#test-resent-otp-code-btn").should('exist')




    })

  

})