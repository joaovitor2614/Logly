import { defineStore } from "pinia"
import { reactive } from "vue"

import api from '../api/api'

interface User {
    name: string,
    email: string,
    id: string,
}

interface UserAPIResponse extends User {
    password?: string
}

export const useUserStore = defineStore('userStore', () => {
    const userInfo: User = reactive({
        name: '',
        _id: ''
    })

    async function getUserInfo() {
        const response = await api.get('users')
        if (response.status === 201) {
            const userData = response.data
            setUserInfo(userData)
        }
    }

    function setUserInfo(userData: UserAPIResponse) {
        delete userData.password
        userInfo.name = userData.name
        userInfo.id = userData.id
        userInfo.email = userData.email
    }


    return {
        userInfo,
        setUserInfo,
        getUserInfo
    }
})