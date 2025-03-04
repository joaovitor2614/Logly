

import { createWebHistory, createRouter } from "vue-router";
import Main from '../Main.vue'
import Register from '../components/auth/Register.vue'
import Login from '../components/auth/Login.vue'
import { registerRouteGuard } from './guard/index'
import type { App } from 'vue';



const routes = [
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/',
    name: 'Main',
    component: Main
  },
]
export const router = createRouter({
  history: createWebHistory(),
  routes
})

export const setupRouter = (app: App) => {

  app.use(router)

  registerRouteGuard(router)
}

