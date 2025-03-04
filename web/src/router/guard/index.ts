import type {
    Router
} from 'vue-router';
import { useAuthStore } from '@/stores/auth'



export const registerRouteGuard = (router: Router) => {
    const publicComponentesRoutes = ['Login', 'Register'];
    
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
}