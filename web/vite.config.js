import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import tailwindcss from '@tailwindcss/vite'

import svgLoader from "vite-svg-loader";

// https://vitejs.dev/config/
export default defineConfig({
  base: "/app/", 
  include: ["plotly.js-dist"],
  plugins: [vue(), svgLoader(), tailwindcss()],
  server: {
    host: true,
    strictPort: true,
    port: 5173,
    proxy: {
        '/api': {
          target: 'http://127.0.0.1:5000/api',
     
          rewrite: (path) => path.replace(/^\/api/, ''),  
        }
      }
  },
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
});
