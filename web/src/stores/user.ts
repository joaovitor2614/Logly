import { defineStore } from "pinia"
import { reactive } from "vue"
import { getUserInfo, putUserInfo, verifyEmailVerificationCode } from '@/api/services/user'
import { useToast } from "vue-toastification"



export const useUserStore = defineStore('userStore', () => {
    const userInfo: App.User.Info = reactive({
        name: '',
        image: '',
        _id: '',
        email: '',
        has_confirmed_email: false
    })
    const toast = useToast()
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

    async function verifyPassedOTPCode(otpCode: string) {
        const response = await verifyEmailVerificationCode(otpCode)
        if (response) {
            toast.success('Account verified successfully!')
            await fetchUser()
        }
    }


    return {
        userInfo,
        setUserInfo,
        editUserInfo,
        verifyPassedOTPCode,
        fetchUser
    }
})