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
  sendResetPasswordCode: {
    path: '/send-reset-password-code',
    name: 'ResetPasswordByCode',
  },
  resetPasswordLink: {
    path: '/reset-password/:token',
    name: 'ResetPasswordLink',
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
  },
  wellLogDataDisplay: {
    path: '/data/:well_id/:well_log_id',
    name: 'WellLogDataDisplay',
  }
}