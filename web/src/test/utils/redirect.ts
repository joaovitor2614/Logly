import { Router } from "vue-router";


export function verifyRedirect(buttonIDName: string, expectedRoutePath: string, router: Router) {
    cy.get(buttonIDName).click();
    cy.wrap(router.isReady()).then(() => {
        cy.wrap(router.currentRoute.value.fullPath).should('eq', expectedRoutePath)
    })
}