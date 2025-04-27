import { AxiosInstance } from "axios";
import { useToast } from "vue-toastification";

const toast = useToast();


const registerResponseInterceptors = (customAPI: AxiosInstance) => {
    customAPI.interceptors.response.use(function (response) {
        return { data: response.data, hasErrors: false};
    }, function (error) {

        toast.error(error.response.data.detail, {
            timeout: 4000
        })
        return { data: undefined, hasErrors: true};
    }
)
}

export default registerResponseInterceptors