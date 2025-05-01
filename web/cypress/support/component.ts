// ***********************************************************
// This example support/component.ts is processed and
// loaded automatically before your test files.
//
// This is a great place to put global configuration and
// behavior that modifies Cypress.
//
// You can change the location of this file or turn off
// automatically serving support files with the
// 'supportFile' configuration option.
//
// You can read more here:
// https://on.cypress.io/configuration
// ***********************************************************

// Import commands.js using ES2015 syntax:
import './commands'
import { createPinia, Pinia, setActivePinia } from "pinia";
import { mount } from 'cypress/vue'
import { DefineComponent } from 'vue';

let pinia: Pinia;

beforeEach(() => {
  pinia = createPinia();

  setActivePinia(pinia);
})

function mountWithPinia(
  Comp: DefineComponent,
  options?: Parameters<typeof mount>[1]
): Cypress.Chainable {
  return mount(Comp, {
    ...options,
    global: {
      ...options?.global,
      plugins: [...(options?.global?.plugins ?? []), pinia],
    },
  });
}

declare global {
  namespace Cypress {
    interface Chainable {
      mountWithPinia: typeof mountWithPinia;
    }
  }
}

Cypress.Commands.add("mountWithPinia", mountWithPinia);
Cypress.Commands.add('mount', mount)

// Example use:
// cy.mount(MyComponent)