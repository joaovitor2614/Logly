const { defineConfig } = require("cypress");

module.exports = defineConfig({
  env: {
    VITE_API_BASE_URL: "http://127.0.0.1:5000/",
    VITE_ACCOUNT_VERIFICATION_REQUIRED: 'true'
  },
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
