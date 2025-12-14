

export const verifySelectorItemsAmount = (selectorId: string, expectedItemsAmount: number) => {
    cy.get(selectorId)
      .parents('.v-input')
      .click()
      cy.get('.v-overlay-container .v-list-item')
      .should('have.length', expectedItemsAmount)

}