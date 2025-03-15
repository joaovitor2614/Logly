

import { createWebHistory, createRouter } from "vue-router";
import Dashboard from '../Dashboard.vue'
import Register from '../components/auth/Register.vue'
import Login from '../components/auth/Login.vue'
import { registerRouteGuard } from './guard/index'
import type { App } from 'vue';
import UserProfile from "../components/profile/UserProfile.vue";



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
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/profile',
    name: 'User Profile',
    component: UserProfile
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

