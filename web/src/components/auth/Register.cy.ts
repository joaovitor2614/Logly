import Register from './Register.vue'
import "vuetify/styles";


describe('<Register />', () => {
  it('renders', () => {
    // see: https://on.cypress.io/mounting-vue
    cy.mountWithPiniaVuetify(Register)
    //cy.get('#test-login-btn').should('be.disabled')
    //cy.get('#test-login-btn').should('be.disabled')
  })
})