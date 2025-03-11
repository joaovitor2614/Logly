import { defineStore } from "pinia"
import { reactive } from "vue"

import api from '../api/api'

interface User {
    name: string,
    email: string,
    _id: string,
}

interface UserAPIResponse extends User {
    password?: string
}

export const useUserStore = defineStore('userStore', () => {
    const userInfo: User = reactive({
        name: '',
        _id: '',
        email: ''
    })

    async function getUserInfo() {
        const response = await api.get('users')
        if (response.status === 200) {

                
            setUserInfo(response.data)
        }
    }

    function setUserInfo(userData: UserAPIResponse) {
        delete userData.password
        userInfo.name = userData.name
        userInfo._id = userData._id
        userInfo.email = userData.email
    }


    return {
        userInfo,
        setUserInfo,
        getUserInfo
    }
})