import type {
    Router
} from 'vue-router';
import { useAuthStore } from '@/stores/auth'



export const registerRouteGuard = (router: Router) => {
   
    
    router.beforeEach(async (to, from) => {
        const authStore = useAuthStore();

        const isLoggedIn = authStore.isAuthenticated;
        if (!isLoggedIn && to.name !== 'Login' && to.name !== 'Register') {
            return { name: 'Login' }
        }
        if (isLoggedIn && to.name !== 'Dashboard') {
            return { name: 'Dashboard' }
        }
    })
}