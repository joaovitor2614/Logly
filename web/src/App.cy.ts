import App from './App.vue'
import { useAuthStore } from './stores'


describe('<App />', () => {
  it('renders', () => {
    const authStore = useAuthStore()
    expect(authStore.isAuthenticated).to.be.false
    cy.mountWithPiniaVuetify(App)
    
  })
})