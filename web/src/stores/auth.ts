import { defineStore } from 'pinia'



interface authState {
    token: string | null,
    isAuthenticated: boolean,
    loading: boolean,
    user: null,
}

export const useAuthStore = defineStore('authStore', {
    state: (): authState => ({
        token: localStorage.getItem('token'),
        isAuthenticated: false,
        loading: true,
        user: null
      })
})