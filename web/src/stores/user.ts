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

    async function fetchUser(): Promise<boolean> {
        const { data: userInfo, hasErrors } = await getUserInfo()
        
        if (!hasErrors) {
            setUserInfo(userInfo)
        }
        return hasErrors
    }

    function setUserInfo(userData: App.User.Info) {
        Object.assign(userInfo, userData)
    }

    async function editUserInfo(userData: Partial<App.User.Info>) {
        
        const { data: updatedUserInfo, hasErrors } = await putUserInfo(userInfo._id, userData)
        if (!hasErrors) {

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