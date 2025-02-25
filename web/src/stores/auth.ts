import { defineStore } from 'pinia'
import { useUserStore } from './user'

import api from '../api/api'



interface UserData {
    name: string
    password: string
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


    
  
    const registerUser = async (userData: UserData) => {
            const response = await api.post('auth/register', userData)
            console.log('response.data', response.data)
            userStore.setUserInfo(response.data)
    }


    return { 
        token,
        isAuthenticated,
        isLoading,
        registerUser
    }
        
})