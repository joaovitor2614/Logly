import type {
    Router
} from 'vue-router';
import { watch } from 'vue';
import { useUserStore, useAuthStore } from '@/stores';
import { getFinalNavigationTarget } from './redirect'





export const registerRouteGuard = (router: Router) => {

    const authStore = useAuthStore();
    const userStore = useUserStore()
    console.log('userStore', userStore.userInfo)
    const hasConfirmedEmail = userStore.userInfo.has_confirmed_email;


    router.beforeEach(async (to, from) => {
        const targetRouteName = to.name as string;
        const isLoggedIn = authStore.isAuthenticated;

        const navigationTarget = getFinalNavigationTarget(isLoggedIn, hasConfirmedEmail, targetRouteName)
     
        if (navigationTarget && navigationTarget !== targetRouteName) {
            return { name: navigationTarget }
        }
    })

    // Escutar alterações no status de autenticação e redirecionar para a tela de login ou dashboard
  
    watch(
        () => authStore.isAuthenticated, // Use a getter function to maintain reactivity
        async (isAuthenticated) => {
            const targetRouteName = router.currentRoute.value.name as string;
            const navigationTarget = getFinalNavigationTarget(isAuthenticated, hasConfirmedEmail, targetRouteName)
            if (navigationTarget && navigationTarget !== targetRouteName) {
                router.push({ name: navigationTarget });
            }

        
       
      },  { immediate: true })

}