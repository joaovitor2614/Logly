import type {
    Router
} from 'vue-router';
import { useAuthStore } from '@/stores/auth'



export const registerRouteGuard = (router: Router) => {
    const authStore = useAuthStore();

    const isLoggedIn = authStore.isAuthenticated;
    console.log('isLoggedIn', isLoggedIn)
    router.beforeEach(async (to, from) => {
        if (!isLoggedIn && to.name !== 'Login' && to.name !== 'Register') {
            return { name: 'Register' }
        }
        if (isLoggedIn && to.name !== 'StarstratumMainApp') {
            return { name: 'StarstratumMainApp' }
        }
    })
}