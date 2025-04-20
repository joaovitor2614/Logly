
import axios from 'axios'
import registerResponseInterceptors from './interceptors';
const api = axios.create({
    baseURL: 'http://127.0.0.1:5000',
    timeout: 10000,
});

registerResponseInterceptors(api)





export default api
