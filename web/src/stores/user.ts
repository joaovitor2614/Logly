import { defineStore } from "pinia"
import { reactive } from "vue"
import { getUserInfo, resetPassword, putUserInfo, verifyEmailVerificationCode, deleteCurrentUserAccount } from '@/api/services/user'
import { useToast } from "vue-toastification"
import { useRouter } from "vue-router"



export const useUserStore = defineStore('userStore', () => {
    const userInfo: App.User.Info = reactive({
        name: '',
        image: '',
        _id: '',
        email: '',
        has_confirmed_email: false
    })
    const toast = useToast()
    const router = useRouter()

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

    async function tryResetPassword(newPassword: string, resetPasswordToken: string) {
        const response = await resetPassword(newPassword, resetPasswordToken)
        if (response) {
            toast.success('Password reset successfully, login to access your account!')
            router.push('/login')
        }
    }

    const deleteUserAccount = async () => {
        const response = await deleteCurrentUserAccount();
        return response
    }


    return {
        userInfo,
        setUserInfo,
        editUserInfo,
        deleteUserAccount,
        tryResetPassword,
        verifyPassedOTPCode,
        fetchUser
    }
})