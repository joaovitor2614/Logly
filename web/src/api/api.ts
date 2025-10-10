
import axios from 'axios'
import registerResponseInterceptors from './interceptors';


const isDev = import.meta.env.DEV;

const api = axios.create({
    baseURL: isDev ? import.meta.env.VITE_API_BASE_URL : '/api',
    timeout: 10000,
});

registerResponseInterceptors(api)





export default api
