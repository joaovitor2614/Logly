import { routesInfo } from '../../info/index'

const PUBLIC_COMPS_ROUTE_INFO_KEYS = ['register', 'landing', 'login', 'sendResetPasswordLink']
console.log('routesInfo', routesInfo)
const PUBLIC_COMPS_NAMES = PUBLIC_COMPS_ROUTE_INFO_KEYS.map(key => routesInfo[key].name)
const accountVerificationRequired = import.meta.env.VITE_ACCOUNT_VERIFICATION_REQUIRED === 'true';

export function getFinalNavigationTarget(
    isAuthenticated: boolean, 
    hasConfirmedEmail: boolean,
    targetRouteName: string,
) {
 
    if (!isAuthenticated) {
        console.log('targetRouteName', targetRouteName)
        if (!PUBLIC_COMPS_NAMES.includes(targetRouteName) || routesInfo.verifyAccount.name == targetRouteName) {
            return routesInfo.login.name
        }
        
    } else {
        console.log('nout ahth')
        if (hasConfirmedEmail || !accountVerificationRequired) {
            if (PUBLIC_COMPS_NAMES.includes(targetRouteName) || routesInfo.verifyAccount.name == targetRouteName) {
                
                return routesInfo.dashboard.name
            }
        } else {
            if (routesInfo.verifyAccount.name != targetRouteName) {
                return routesInfo.verifyAccount.name;
            }
        }
    }
    return null
}