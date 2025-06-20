import { useAuthStore } from '@/stores'
import Header from './Header.vue'



describe('<Header />', () => {
  it('renders', () => {
    // see: https://on.cypress.io/mounting-vue
    cy.mountWithPiniaVuetify(Header)

  })
  it('does not show authenticated only visible buttons when not authenticated', () => {
    cy.mountWithPiniaVuetify(Header).then(() => {
      cy.get('#test-logout-btn').should('not.exist')
      cy.get('#test-header-login-btn').should('exist')
      cy.get('#test-header-register-btn').should('exist')
    })
  })
  it('does show authenticated only visible buttons when authenticated and not account verified', () => {
    cy.mountWithPiniaVuetify(Header).then(() => {
      const authStore = useAuthStore();

      authStore.isAuthenticated = true

      

      cy.get('#test-logout-btn').should('exist')
      cy.get('#test-header-login-btn').should('not.exist')
      cy.get('#test-header-register-btn').should('not.exist')
    })
  })


})