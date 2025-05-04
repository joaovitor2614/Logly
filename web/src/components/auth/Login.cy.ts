import Login from './Login.vue'



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
})