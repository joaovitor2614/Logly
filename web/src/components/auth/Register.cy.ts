import Register from './Register.vue'
import { verifyRedirect } from '@/test/utils/redirect'

describe('<Register />', () => {
  it('renders', () => {
    // see: https://on.cypress.io/mounting-vue
    cy.mountWithPiniaVuetify(Register)

    cy.get('#test-register-btn').should('be.disabled')


    cy.get('#test-email-input').type('joao@gmail.com')
    cy.get('#test-password-input').type('123456')

    cy.get('#test-confirm-password-input').type('123456')
    cy.get('#test-register-btn').should('be.disabled')


    cy.get('#test-name-input').type('João Vitor')
    cy.get('#test-register-btn').should('be.enabled')
    it('redirects to login page when clicking button', () => {
      cy.mountWithPiniaVuetify(Register).then(({router}) => {
        verifyRedirect('#test-redirect-to-login-btn', '/login', router)

      })
      
      })
    })
})