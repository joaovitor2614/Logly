import { RouteInfo } from "../types";


export const routesInfo: Record<string, RouteInfo> = {
  register: {

    path: '/register',
    name: 'Register',
  },
  login: {
    path: '/login',
    name: 'Login',
  },
  landing: {
    path: '/',
    name: 'Landing',
  },
  sendResetPasswordLink: {
    path: '/send-reset-password-link',
    name: 'SendResetPasswordLink',
  },
  dashboard: {
    path: '/dashboard',
    name: 'Dashboard',
  },
  verifyAccount: {
    path: '/verify-account',
    name: 'VerifyAccount',
  },
  billing: {
    path: '/billing',
    name: 'Billing',
  }
}