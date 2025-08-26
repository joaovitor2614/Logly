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
    cors: import.meta.env.VITE_API_BASE_URL,
  },
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
});
