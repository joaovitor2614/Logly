import type {
    Router
} from 'vue-router';
import { watch } from 'vue';
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
        console.log('router before')
        const navigationTarget = getFinalNavigationTarget(isLoggedIn, hasConfirmedEmail, targetRouteName)
     
        if (navigationTarget && navigationTarget !== targetRouteName) {
            return { name: navigationTarget }
        }
    })
    watch(() => [authStore.isAuthenticated, userStore.userInfo.has_confirmed_email], () => {
        const hasConfirmedEmail = userStore.userInfo.has_confirmed_email;
        const isAuthenticated = authStore.isAuthenticated
        console.log('watch')
        const targetRouteName = router.currentRoute.value.name as string;
        const navigationTarget = getFinalNavigationTarget(isAuthenticated, hasConfirmedEmail, targetRouteName)
        if (navigationTarget && navigationTarget !== targetRouteName) {
            router.push({ name: navigationTarget });
        }

    }, { immediate: true })



}