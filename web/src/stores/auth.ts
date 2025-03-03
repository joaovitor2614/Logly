import { defineStore } from 'pinia'
import { useUserStore } from './user'
import { ref, type Ref } from 'vue'
import { setAPIHeadersBearerToken} from '../api/utils'
import api from '../api/api'



interface NewUserData {
    name: string;
    password: string;
    email: string
}

interface UserCrendentials {
    name: string;
    password: string;

}
/*
state: (): authState => ({
        token: localStorage.getItem('token'),
        isAuthenticated: true,
        loading: true,
        user: null
    }),

*/

export const useAuthStore = defineStore('authStore', () => {
    const token: Ref<string | null> = ref(localStorage.getItem('token'))
    const isAuthenticated = ref(true);
    const isLoading = ref(false);
    const userStore = useUserStore()


    
  
    const registerUser = async (userData: NewUserData) => {
            const response = await api.post('auth/register', userData)
            if (response.status === 201) {
                token.value = response.data.token;
                localStorage.setItem('token', response.data.token)
                setAPIHeadersBearerToken(token.value)
                
                userStore.getUserInfo();

                isAuthenticated.value = true;
            }
            return response
    }

    const loginUser = async (userData: UserCrendentials) => {
            const response = await api.post('auth/login', userData)
            if (response.status === 201) {
                token.value = response.data.token;
                localStorage.setItem('token', response.data.token)
                setAPIHeadersBearerToken(token.value)
                userStore.getUserInfo();

                isAuthenticated.value = true;
                
                
            }
            return response
        }
            


    return { 
        token,
        isAuthenticated,
        isLoading,
        loginUser,
        registerUser
    }
        
})