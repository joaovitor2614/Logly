
import axios from 'axios'
import registerResponseInterceptors from './interceptors';


const isDev = import.meta.env.DEV;

const api = axios.create({
    baseURL: '/api',
    timeout: 10000,
});

registerResponseInterceptors(api)





export default api
