import { defineStore } from "pinia"
import { reactive } from "vue"
import { getUserInfo, editUserInfo, putUserInfo } from '@/api/services/user'
import api from '../api/api'


export const useUserStore = defineStore('userStore', () => {
    const userInfo: Api.User.Info = reactive({
        name: '',
        image: '',
        _id: '',
        email: ''
    })

    async function fetchUser() {
        const response = await getUserInfo()
        
        if (response.status === 200) {

                
            setUserInfo(response.data)
        }
    }

    function setUserInfo(userData: Api.User.Info) {
        Object.assign(userInfo, userData)
    }

    async function editUserInfo(userData: Api.User.Info) {
        const response = await putUserInfo(userData)
        if (response) {
            const editedUserInfo = response.data
            Object.assign(userInfo, editedUserInfo)
        }
    }


    return {
        userInfo,
        setUserInfo,
        fetchUser
    }
})