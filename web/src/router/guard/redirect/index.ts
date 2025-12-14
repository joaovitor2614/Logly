import { routesInfo } from '../../info/index'

const PUBLIC_COMPS_ROUTE_INFO_KEYS = ['register', 'landing', 'login', 'sendResetPasswordCode', 'resetPasswordLink']

const PUBLIC_COMPS_NAMES = PUBLIC_COMPS_ROUTE_INFO_KEYS.map(key => routesInfo[key].name)
const accountVerificationRequired = import.meta.env.VITE_ACCOUNT_VERIFICATION_REQUIRED === 'true';

export function getFinalNavigationTarget(
    isAuthenticated: boolean, 
    hasConfirmedEmail: boolean,
    targetRouteName: string,
): string | undefined {

    const isTryingToAccessPublicComp = PUBLIC_COMPS_NAMES.includes(targetRouteName);

    if (!isAuthenticated) {
        return !isTryingToAccessPublicComp ? routesInfo.login.name : undefined
    }

    // Authenticated users but email not verified
    if (!hasConfirmedEmail && accountVerificationRequired) {
        return routesInfo.verifyAccount.name !== targetRouteName ? routesInfo.verifyAccount.name : undefined
    }




      // Authenticated users should not access public routes 
    if (isTryingToAccessPublicComp || routesInfo.verifyAccount.name === targetRouteName) {
        return routesInfo.dashboard.name
    }

    return undefined
  
}