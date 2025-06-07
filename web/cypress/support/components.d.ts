/// <reference types="cypress" />
import { DefineComponent } from 'vue';

declare namespace Cypress {
  interface Chainable {
    mountWithPiniaVuetify(
      Comp: DefineComponent,
      options?: Parameters<typeof import('cypress/vue').mount>[1]
    ): Cypress.Chainable<{ router: ReturnType<typeof import('@/router/router').createRouterInstance> }>;

    mount: typeof import('cypress/vue').mount;
  }
}