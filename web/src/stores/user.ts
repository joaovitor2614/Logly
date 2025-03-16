import { defineStore } from "pinia"
import { reactive } from "vue"

import api from '../api/api'


export const useUserStore = defineStore('userStore', () => {
    const userInfo: Api.User.Info = reactive({
        name: '',
        image: '',
        _id: '',
        email: ''
    })

    async function getUserInfo() {
        const response = await api.get<Api.User.Info>('users')
       
        if (response.status === 200) {

                
            setUserInfo(response.data)
        }
    }

    function setUserInfo(userData: Api.User.Info) {
        Object.assign(userInfo, userData)
    }


    return {
        userInfo,
        setUserInfo,
        getUserInfo
    }
})