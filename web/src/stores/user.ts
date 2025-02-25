import { defineStore } from "pinia"
import { reactive } from "vue"

interface User {
    name: string,
    _id: string,
}

interface UserAPIResponse extends User {
    password?: string
}

export const useUserStore = defineStore('userStore', () => {
    const userInfo: User = reactive({
        name: '',
        _id: ''
    })

    function setUserInfo(userData: UserAPIResponse) {
        delete userData.password
        userInfo.name = userData.name
        userInfo._id = userData._id
    }


    return {
        userInfo,
        setUserInfo
    }
})