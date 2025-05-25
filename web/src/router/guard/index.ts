import type {
    Router
} from 'vue-router';
import { useAuthStore } from '@/stores/auth'
import { watch } from 'vue';



export const registerRouteGuard = (router: Router) => {
    const publicComponentesRoutes = ['Login', 'Register', 'Landing'];
    
    router.beforeEach(async (to, from) => {
        const authStore = useAuthStore();

        const isLoggedIn = authStore.isAuthenticated;
        if (!isLoggedIn && !publicComponentesRoutes.includes(to.name as string)) {
            return { name: 'Login' }
        }
        if (isLoggedIn && publicComponentesRoutes.includes(to.name as string)) {
            return { name: 'Dashboard' }
        }
    })

    // Escutar alterações no status de autenticação e redirecionar para a tela de login ou dashboard
    const authStore = useAuthStore()
    watch(
        () => authStore.isAuthenticated, // Use a getter function to maintain reactivity
        async (isAuthenticated) => {
            if (!isAuthenticated && !publicComponentesRoutes.includes(router.currentRoute.value.name as string)) {
                router.push({ name: 'Login' });
            } else if (isAuthenticated && publicComponentesRoutes.includes(router.currentRoute.value.name as string)) {
                router.push({ name: 'Dashboard' });
            }
        
       
      },  { immediate: true })




}