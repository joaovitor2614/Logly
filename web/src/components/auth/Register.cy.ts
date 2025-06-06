import Register from './Register.vue'
import "vuetify/styles";


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
      cy.mountWithPiniaVuetify(Login).then(({router}) => {
        cy.get('#test-redirect-to-login-btn').click();
        cy.wrap(router.isReady()).then(() => {
          cy.wrap(router.currentRoute.value.fullPath).should('eq', '/login')
        })
      })
      
      })
    })
})