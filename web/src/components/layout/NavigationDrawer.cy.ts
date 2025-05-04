import NavigationDrawer from './NavigationDrawer.vue'



describe('<NavigationDrawer />', () => {
  it('renders', () => {
    // see: https://on.cypress.io/mounting-vue
    cy.mountWithPiniaVuetify(NavigationDrawer)
  })
})