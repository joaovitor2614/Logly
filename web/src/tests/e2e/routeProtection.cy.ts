import { useAuthStore } from "@/stores"

describe('Route Protection Tests', () => {
  it('Should be redicted to Login Page', () => {
    cy.visit('/')
    cy.url().should('include', 'login') // => true 
  })
})