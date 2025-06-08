import Login from './Login.vue'
import { verifyRedirect } from '@/test/utils/redirect'


describe('<Login />', () => {
  it('renders', () => {
    // see: https://on.cypress.io/mounting-vue
    cy.mountWithPiniaVuetify(Login)
    cy.get('#test-login-btn').should('be.disabled')
    

    // Insert valid form values
    cy.get('#test-email-input').type('joao@gmail.com')
    cy.get('#test-password-input').type('123456')

    // Now the buttn should be enabled
    cy.get('#test-login-btn').should('be.enabled')
  })
  it('redirects to register page when clicking button', () => {
    cy.mountWithPiniaVuetify(Login).then(({router}) => {
      verifyRedirect('#test-redirect-to-register-btn', '/register', router)
    })
    
  })

})