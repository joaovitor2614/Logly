import { routesInfo } from '../../info/index'

const PUBLIC_COMPS_ROUTE_INFO_KEYS = ['register', 'landing', 'login']
const PUBLIC_COMPS_NAMES = PUBLIC_COMPS_ROUTE_INFO_KEYS.map(key => routesInfo[key].name)

export function getFinalNavigationTarget(
    isAuthenticated: boolean, 
    hasConfirmedEmail: boolean,
    targetRouteName: string,
) {
    console.log('hasConfirmedEmail', hasConfirmedEmail, isAuthenticated)
    if (!isAuthenticated) {
        if (!PUBLIC_COMPS_NAMES.includes(targetRouteName) || routesInfo.verifyAccount.name == targetRouteName) {
            return routesInfo.login.name
        }
        
    } else {
        if (hasConfirmedEmail) {
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