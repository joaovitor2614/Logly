import WellImport from './WellImport.vue'



describe('<WellImport />', () => {
  it('renders', () => {
    cy.get('#test-import-well-btn').should('be.disabled')
    cy.get('#test-well-name-input').type('Poço1')
    cy.get('#test-las-file-input').type('./my-las-file-path.las')

    cy.get('#test-import-well-btn').should('be.enabled')
})
})