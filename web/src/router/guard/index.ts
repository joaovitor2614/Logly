import type {
    Router
} from 'vue-router';
import { watch } from 'vue';
import { useUserStore, useAuthStore } from '@/stores';

const UNIQUE_COMPONENTS_NAMES = {
    public: ['Login', 'Register', 'Landing'],
    not_verified: ['VerifyAccount']
}

export const registerRouteGuard = (router: Router) => {
    const publicComponentesRoutes = ['Login', 'Register', 'Landing'];
    
    router.beforeEach(async (to, from) => {
        const authStore = useAuthStore();
        const userStore = useUserStore()
        const isLoggedIn = authStore.isAuthenticated;
        console.log('here', isLoggedIn)
        console.log('userStore.userInfo.has_confirmed_email ', userStore.userInfo.has_confirmed_email )
        if (!isLoggedIn && !UNIQUE_COMPONENTS_NAMES.public.includes(to.name as string)) {
            return { name: 'Login' }
        }
        if (isLoggedIn) {
            if (userStore.userInfo.has_confirmed_email && UNIQUE_COMPONENTS_NAMES.public.includes(to.name as string)) {
                return { name: 'Dashboard' }
            } else if (!userStore.userInfo.has_confirmed_email && !UNIQUE_COMPONENTS_NAMES.not_verified.includes(to.name as string)) {
                return { name: 'VerifyAccount' }

            }
            
        }
    })

    // Escutar alterações no status de autenticação e redirecionar para a tela de login ou dashboard
    const authStore = useAuthStore()
    watch(
        () => authStore.isAuthenticated, // Use a getter function to maintain reactivity
        async (isAuthenticated) => {
            const userStore = useUserStore()
            if (!isAuthenticated && !publicComponentesRoutes.includes(router.currentRoute.value.name as string)) {
                router.push({ name: 'Login' });
            } else if (isAuthenticated) {
                if (userStore.userInfo.has_confirmed_email && publicComponentesRoutes.includes(router.currentRoute.value.name as string)) {
                    router.push({ name: 'Dashboard' });
                } else if (!userStore.userInfo.has_confirmed_email && !UNIQUE_COMPONENTS_NAMES.not_verified.includes(router.currentRoute.value.name as string)) {
                    router.push({ name: 'VerifyAccount' });
                }
                
            }
        
       
      },  { immediate: true })

}