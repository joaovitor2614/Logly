import type {
    Router
} from 'vue-router';
import { watch } from 'vue';
import { useUserStore, useAuthStore } from '@/stores';
import { routesInfo } from '../info/index'
const UNIQUE_COMPONENTS_NAMES = {
    public: ['Login', 'Register', 'Landing'],
    not_verified: ['VerifyAccount']
}

export const registerRouteGuard = (router: Router) => {
    const publicComponentsRoutesInfoKeys = ['register', 'landing', 'login']
    const publicComponentesRoutes = publicComponentsRoutesInfoKeys.map(publicComponentRouteInfoKey => routesInfo[publicComponentRouteInfoKey]);
    const authStore = useAuthStore();
    const userStore = useUserStore()
    router.beforeEach(async (to, from) => {

        const isLoggedIn = authStore.isAuthenticated;
        console.log('here', isLoggedIn)
        console.log('userStore.userInfo.has_confirmed_email ', userStore.userInfo.has_confirmed_email )
        if (!isLoggedIn && !UNIQUE_COMPONENTS_NAMES.public.includes(to.name as string)) {
            return { name: routesInfo.login.name }
        }
        if (isLoggedIn) {
            if (userStore.userInfo.has_confirmed_email && UNIQUE_COMPONENTS_NAMES.public.includes(to.name as string)) {
                return { name: routesInfo.dashboard.name }
            } else if (!userStore.userInfo.has_confirmed_email && !UNIQUE_COMPONENTS_NAMES.not_verified.includes(to.name as string)) {
                return { name: routesInfo.verifyAccount.name }

            }
            
        }
    })

    // Escutar alterações no status de autenticação e redirecionar para a tela de login ou dashboard
  
    watch(
        () => authStore.isAuthenticated, // Use a getter function to maintain reactivity
        async (isAuthenticated) => {

            if (!isAuthenticated && !publicComponentesRoutes.includes(router.currentRoute.value.name as string)) {
                router.push({ name: routesInfo.login.name });
            } else if (isAuthenticated) {
                if (userStore.userInfo.has_confirmed_email && publicComponentesRoutes.includes(router.currentRoute.value.name as string)) {
                    router.push({ name: routesInfo.dashboard.name });
                } else if (!userStore.userInfo.has_confirmed_email && !UNIQUE_COMPONENTS_NAMES.not_verified.includes(router.currentRoute.value.name as string)) {
                    router.push({ name: routesInfo.verifyAccount.name });
                }
                
            }
        
       
      },  { immediate: true })

}