import { defineStore } from "pinia"
import { reactive } from "vue"
import { getUserInfo, putUserInfo } from '@/api/services/user'



export const useUserStore = defineStore('userStore', () => {
    const userInfo: App.User.Info = reactive({
        name: '',
        image: '',
        _id: '',
        email: ''
    })

    async function fetchUser() {
        const response = await getUserInfo()
        
        if (response) {
            const userInfo = response.data
            setUserInfo(userInfo)
        }
        return response
    }

    function setUserInfo(userData: App.User.Info) {
        Object.assign(userInfo, userData)
    }

    async function editUserInfo(userData: Partial<App.User.Info>) {
        
        const response = await putUserInfo(userInfo._id, userData)
        if (response) {
            const updatedUserInfo = response.data
            Object.assign(userInfo, updatedUserInfo)
        }
    }


    return {
        userInfo,
        setUserInfo,
        editUserInfo,
        fetchUser
    }
})