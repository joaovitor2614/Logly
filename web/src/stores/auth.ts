import { defineStore } from 'pinia'
import { useUserStore } from './user'
import api from '../api/api'


interface authState {
    token: string | null,
    isAuthenticated: boolean,
    loading: boolean,
    user: null,
}

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
    const isAuthenticated = true;
    const isLoading = false;

    const userStore = useUserStore()

    
    actions: {
    const registerUser = async (userData: UserData) =>{
            const response = await api.post('auth/register', userData)
        }
    }

    return [ 
        token,
        isAuthenticated,
        isLoading,
        userStore
    ]
}