import { defineStore } from 'pinia'
import { ref, type Ref } from 'vue'
import { useToast } from "vue-toastification";
import api from '../api/api'


export const useAuthStore = defineStore('authStore', () => {
    const token: Ref<string | null> = ref(localStorage.getItem('token'))
    const isAuthenticated = ref(false);
    const isLoading = ref(false);
    const toast = useToast();



    /**
     * Handles user registration and login by calling the API.
     * If the response is 201, sets the JWT token in local storage and updates the user info.
     * If the response is not 201, shows a toast error message with the status text.
     * @param authType - 'register' or 'login'
     * @param userData - user data to be sent to the API
     */
    const executeAuthAction = async (authType: 'register' | 'login', userData: App.User.Register | App.User.Login) => {
        try {
            
            const response = await api.post<Api.Auth.Token>(`auth/${authType}`, userData);
            token.value = response.data.token;

            toast.success(`User ${authType === 'register' ? 'registered' : 'logged in'} successfully!`);

        } catch (error) {
            console.log('error', error)
            toast.error(error.response.data.detail);
        }
    
    }


    const logout = () => {
        token.value = null
    }


    
  
    const registerUser = async (userData: App.User.Register) => {
        executeAuthAction('register', userData)
    }

    const loginUser = async (userData: App.User.Login) => {
        executeAuthAction('login', userData)
            
    }
            
    return { 
        token,
        logout,
        isAuthenticated,
        isLoading,
        loginUser,
        registerUser
    }
        
})