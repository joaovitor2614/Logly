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
        const { userInfo, hasErrors } = await getUserInfo()
        
        if (!hasErrors) {
            setUserInfo(userInfo)
        }
    }

    function setUserInfo(userData: App.User.Info) {
        Object.assign(userInfo, userData)
    }

    async function editUserInfo(userData: App.User.Info) {
        const { updatedUserInfo, hasErrors } = await putUserInfo(userData)
        if (!hasErrors) {

            Object.assign(userInfo, updatedUserInfo)
        }
    }


    return {
        userInfo,
        setUserInfo,
        fetchUser
    }
})