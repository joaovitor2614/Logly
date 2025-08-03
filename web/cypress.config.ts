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
      specPattern: 'src/components/**/*.cy.{js,ts}',

    },
  },

  e2e: {
    baseUrl: 'http://localhost:5173',
    testIsolation: true,
    supportFile: 'cypress/support/e2e.ts',
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
