import type {
    Router
} from 'vue-router';
import { watchEffect } from 'vue';
import { useUserStore, useAuthStore } from '@/stores';
import { getFinalNavigationTarget } from './redirect'





export const registerRouteGuard = (router: Router) => {




    const authStore = useAuthStore();
    const userStore = useUserStore();
    
            

    router.beforeEach(async (to, from) => {

        const userStore = useUserStore()
        const hasConfirmedEmail = userStore.userInfo.has_confirmed_email;
       
        const targetRouteName = to.name as string;
        const isLoggedIn = authStore.isAuthenticated;

        const navigationTarget = getFinalNavigationTarget(isLoggedIn, hasConfirmedEmail, targetRouteName)
     
        if (navigationTarget && navigationTarget !== targetRouteName) {
            return { name: navigationTarget }
        }
    })

    // Escutar alterações no status de autenticação e redirecionar para a tela de login ou dashboard
    watchEffect(() => {

        const hasConfirmedEmail = userStore.userInfo.has_confirmed_email;
        const isAuthenticated = authStore.isAuthenticated
        console.log('watchEffect', hasConfirmedEmail, isAuthenticated)
        const targetRouteName = router.currentRoute.value.name as string;
        const navigationTarget = getFinalNavigationTarget(isAuthenticated, hasConfirmedEmail, targetRouteName)
        if (navigationTarget && navigationTarget !== targetRouteName) {
            router.push({ name: navigationTarget });
        }

    })


}