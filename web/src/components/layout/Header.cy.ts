
import { verifyRedirect } from '@/test/utils/redirect'
import Header from './Header.vue'

const redirectTestCasesInfo = [
  {
    expectedRoutePath: '/login',
    redirectionBtnIDName: '#test-header-login-btn',
  },
  {
    expectedRoutePath: '/register',
    redirectionBtnIDName: '#test-header-register-btn',
  }
]

describe('<Header />', () => {
  it('renders', () => {
    // see: https://on.cypress.io/mounting-vue
    cy.mountWithPiniaVuetify(Header)

  })
  redirectTestCasesInfo.forEach((redirectTestCaseInfo) => {
      it(`redirects to ${redirectTestCaseInfo.expectedRoutePath} when clicking button`, () => {
        cy.mountWithPiniaVuetify(Header).then(({router}) => {
          verifyRedirect(redirectTestCaseInfo.redirectionBtnIDName, redirectTestCaseInfo.expectedRoutePath, router)
        })
      })
    })
})