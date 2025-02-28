import { defineStore } from 'pinia'
import { useUserStore } from './user'

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
    const token = localStorage.getItem('token')
    const isAuthenticated = false;
    const isLoading = false;
    const userStore = useUserStore()


    
  
    const registerUser = async (userData: NewUserData) => {
            const response = await api.post('auth/register', userData)
            if (response.status === 201) {
                console.log('response.data.token', response.data.token)
                localStorage.setItem('token', response.data.token)
            }
    }

    const loginUser = async (userData: UserCrendentials) => {
            const response = await api.post('auth/login', userData)
            if (response.status === 201) {
                localStorage.setItem('token', response.data.token)
            }
        }
            


    return { 
        token,
        isAuthenticated,
        isLoading,
        registerUser
    }
        
})