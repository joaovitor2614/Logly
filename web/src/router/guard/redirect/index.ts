import { routesInfo } from '../../info/index'

const PUBLIC_COMPS_ROUTE_INFO_KEYS = ['register', 'landing', 'login', 'sendResetPasswordLink', 'resetPasswordLink']

const PUBLIC_COMPS_NAMES = PUBLIC_COMPS_ROUTE_INFO_KEYS.map(key => routesInfo[key].name)
const accountVerificationRequired = import.meta.env.VITE_ACCOUNT_VERIFICATION_REQUIRED === 'true';

export function getFinalNavigationTarget(
    isAuthenticated: boolean, 
    hasConfirmedEmail: boolean,
    targetRouteName: string,
): string | undefined {
    console.log('targetRouteName', targetRouteName)
    const isTryingToAccessPublicComp = PUBLIC_COMPS_NAMES.includes(targetRouteName);

    if (!isAuthenticated) {
        if (!isTryingToAccessPublicComp) {
            return routesInfo.login.name
        }
        
    } else {
 
        if (!hasConfirmedEmail && accountVerificationRequired) {
            if (routesInfo.verifyAccount.name !== targetRouteName) {
                return routesInfo.verifyAccount.name;
            }
        } 
        else if (isTryingToAccessPublicComp) {
            return routesInfo.dashboard.name
        }
    }
    return undefined
  
}