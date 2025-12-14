import { routesInfo } from '@/router/info'
import Login from './Login.vue'
import { verifyRedirect } from '@/test/utils/redirect'


const redirectTestCasesInfo = [
  {
    expectedRoutePath: routesInfo.register.path,
    redirectionBtnIDName: '#test-redirect-to-register-btn',
  },
  {
    expectedRoutePath: routesInfo.sendResetPasswordCode.path,
    redirectionBtnIDName: '#test-forgot-password-btn',
  },

]


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
  redirectTestCasesInfo.forEach((redirectTestCaseInfo) => {
    it(`redirects to ${redirectTestCaseInfo.expectedRoutePath} when clicking button`, () => {
      cy.mountWithPiniaVuetify(Login).then(({router}) => {
        verifyRedirect(redirectTestCaseInfo.redirectionBtnIDName, redirectTestCaseInfo.expectedRoutePath, router)
      })
      
    })
  })


})