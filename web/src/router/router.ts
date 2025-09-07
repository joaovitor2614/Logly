
import { createWebHistory, createRouter, createMemoryHistory } from "vue-router";
import Dashboard from '../Dashboard.vue'
import Register from '../components/auth/Register.vue'
import Login from '../components/auth/Login.vue'
import LandingPage from '../components/landing/LandingPage.vue'

import VerifyAccountByCode from "@/components/verify/VerifyAccountByCode.vue";
import SendResetPasswordLink from "../components/verify/SendResetPasswordLink.vue";
import { registerRouteGuard } from './guard/index'
import type { App } from 'vue';
import { routesInfo } from './info'
import ResetPassword from "@/components/verify/ResetPassword.vue";




const routes = [
  {
    path: routesInfo.register.path,
    name: routesInfo.register.name,
    component: Register
  },
  {
    path: routesInfo.sendResetPasswordLink.path,
    name: routesInfo.sendResetPasswordLink.name,
    component: SendResetPasswordLink
  },
  {
    path: routesInfo.resetPasswordLink.path,
    name: routesInfo.resetPasswordLink.name,
    component: ResetPassword
  },
  {
    path: routesInfo.login.path,
    name: routesInfo.login.name,
    component: Login
  },
  {
    path: routesInfo.landing.path,
    name: routesInfo.landing.name,
    component: LandingPage
  },
  {
    path: routesInfo.dashboard.path,
    name: routesInfo.dashboard.name,
    component: Dashboard
  },
  {
    path: routesInfo.verifyAccount.path,
    name: routesInfo.verifyAccount.name,
    component: VerifyAccountByCode
  },
]

export function createRouterInstance(is_test: boolean = false) {
  return createRouter({
  history: is_test ? createMemoryHistory() : createWebHistory(),
  routes
})

}
export const router = createRouterInstance()

export const setupRouter = (app: App) => {

  app.use(router)

  registerRouteGuard(router)

}

