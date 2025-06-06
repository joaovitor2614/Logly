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
import { createRouterInstance } from '@/router/router'
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

let pinia: Pinia;

beforeEach(() => {
  pinia = createPinia();

  setActivePinia(pinia);
})

const vuetify = createVuetify({
  components,
  directives,
});

function mountWithPiniaVuetify(
  Comp: DefineComponent,
  options?: Parameters<typeof mount>[1]
): Cypress.Chainable {
  const router = createRouterInstance(true)
  return mount(Comp, {
    ...options,
    global: {
      ...options?.global,
      plugins: [...(options?.global?.plugins ?? []), pinia, vuetify, router],
    },
  }).then(() => {
    return { router }
  })
}

declare global {
  namespace Cypress {
    interface Chainable {
      mountWithPinia: typeof mountWithPinia;
    }
  }
}

Cypress.Commands.add("mountWithPiniaVuetify", mountWithPiniaVuetify);
Cypress.Commands.add('mount', mount)

// Example use:
// cy.mount(MyComponent)