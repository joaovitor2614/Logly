
import { createWebHistory, createRouter } from "vue-router";
import Dashboard from '../Dashboard.vue'
import Register from '../components/auth/Register.vue'
import Login from '../components/auth/Login.vue'
import LandingPage from '../components/landing/LandingPage.vue'
import BillingPlanSelection from '../components/billing/BillingPlanSelection.vue'
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
    name: 'Landing',
    component: LandingPage
  },
  {
    path: '/billing',
    name: 'Billing',
    component: BillingPlanSelection
  },
  {
    path: '/dashbaord',
    name: 'Dashboard',
    component: Dashboard
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

