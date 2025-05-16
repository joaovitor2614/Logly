
import axios from 'axios'
import registerResponseInterceptors from './interceptors';
const api = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL,
    timeout: 10000,
});

registerResponseInterceptors(api)





export default api
