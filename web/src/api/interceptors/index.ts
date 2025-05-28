import { AxiosInstance } from "axios";
import { useToast } from "vue-toastification";

const toast = useToast();


const registerResponseInterceptors = (customAPI: AxiosInstance) => {
    customAPI.interceptors.response.use(function (response) {
        return response
    }, function (error) {

        toast.error(error.response.data.detail, {
            timeout: 4000
        })
        return undefined
    }
)
}

export default registerResponseInterceptors