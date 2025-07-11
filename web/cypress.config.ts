const { defineConfig } = require("cypress");

module.exports = defineConfig({
  component: {
    devServer: {
      framework: "vue",
      bundler: "vite",
    },
  },

  e2e: {
    baseUrl: 'http://localhost:5173',
    testIsolation: true,
    supportFile: 'cypress/support/e2e.ts',
    specPattern: 'src/tests/e2e/**/*.cy.{js,ts}',
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
