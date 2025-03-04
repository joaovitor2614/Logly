import { defineStore } from 'pinia'
import { useUserStore } from './user'
import { ref, type Ref } from 'vue'
import { router } from '../router/router'
import { setAPIHeadersBearerToken} from '../api/utils'
import { useToast } from "vue-toastification";
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
    const isAuthenticated = ref(false);
    const isLoading = ref(false);
    const userStore = useUserStore()
    const toast = useToast();


    /**
     * Handles user registration and login by calling the API.
     * If the response is 201, sets the JWT token in local storage and updates the user info.
     * If the response is not 201, shows a toast error message with the status text.
     * @param authType - 'register' or 'login'
     * @param userData - user data to be sent to the API
     */
    const executeAuthAction = async (authType: 'register' | 'login', userData: NewUserData | UserCrendentials) => {
        const response = await api.post(`auth/${authType}`, userData)
        if (response.status === 201) {
            localStorage.setItem('token', response.data.token)
            setAPIHeadersBearerToken(token.value);
            userStore.getUserInfo();
            isAuthenticated.value = true;
            router.push('/')
        }
        if (response.status == 201) {
            toast.success(`User ${authType === 'register' ? 'registered' : 'logged in'} successfully!`);
        } else {
            toast.error(!response ? 'User registration failed!' : `${response.status} - ${response.statusText}`);
        }
    
    }


    
  
    const registerUser = async (userData: NewUserData) => {
        executeAuthAction('register', userData)
    }

    const loginUser = async (userData: UserCrendentials) => {
        executeAuthAction('login', userData)
            
    }
            
    return { 
        token,
        isAuthenticated,
        isLoading,
        loginUser,
        registerUser
    }
        
})