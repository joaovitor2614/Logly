import { AxiosInstance } from "axios";
import { useToast } from "vue-toastification";

const toast = useToast();


const registerResponseInterceptors = (customAPI: AxiosInstance) => {
    customAPI.interceptors.response.use(function (response) {
        return { data: response.data, hasErrors: false};
    }, function (error) {
        console.log('error.response', error.response)
        toast.error(error.response.data.message, {
            timeout: 4000
        })
        return { data: undefined, hasErrors: true};
    }
)
}

export default registerResponseInterceptors