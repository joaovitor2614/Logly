import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import tailwindcss from '@tailwindcss/vite'

import svgLoader from "vite-svg-loader";

// https://vitejs.dev/config/
export default defineConfig({
  include: ["plotly.js-dist"],
  plugins: [vue(), svgLoader(), tailwindcss()],
  server: {
    host: true,
    strictPort: true,
    port: 5173,
    cors: "https://logly-api-f5e0fb6df0c0.herokuapp.com/",
  },
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
});
