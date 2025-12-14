
import { createWebHistory, createRouter, createMemoryHistory } from "vue-router";
import Dashboard from '../Dashboard.vue'
import Register from '../components/auth/Register.vue'
import Login from '../components/auth/Login.vue'
import LandingPage from '../components/landing/LandingPage.vue'

import VerifyAccountByCode from "@/components/verify/VerifyAccountByCode.vue";
import ResetPasswordByCode from "../components/verify/ResetPasswordByCode.vue";
import { registerRouteGuard } from './guard/index'
import type { App } from 'vue';
import { routesInfo } from './info'
import ResetPassword from "@/components/verify/ResetPasswordForm.vue";
import WellLogDataDisplay from "@/components/welllog/WellLogDataDisplay.vue";




const routes = [
  {
    path: routesInfo.register.path,
    name: routesInfo.register.name,
    component: Register
  },
  {
    path: routesInfo.sendResetPasswordCode.path,
    name: routesInfo.sendResetPasswordCode.name,
    component: ResetPasswordByCode
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
  {
    path: routesInfo.wellLogDataDisplay.path,
    name: routesInfo.wellLogDataDisplay.name,
    component: WellLogDataDisplay
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

