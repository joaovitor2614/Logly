import { useAuthStore } from "@/stores"

describe('Route Protection Tests', () => {
  it('Should be redicted to Login Page', () => {
    cy.visit('/')
    cy.url().should('include', 'login') // => true 
  })
  it('Should be redicted to Verify Account Page', () => {
    const authStore = useAuthStore();
    authStore.isAuthenticated = true
    authStore.userInfo['has_confirmed_email'] = false
    cy.visit('/')
    cy.url().should('include', 'verify-account') // => true 
  })
})