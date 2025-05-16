
import axios from 'axios'
import registerResponseInterceptors from './interceptors';
const api = axios.create({
    baseURL: 'https://mamata-ou-cilada-serve-git-f4529e-joao-vitors-projects-80c25497.vercel.app/',
    timeout: 10000,
});

registerResponseInterceptors(api)





export default api
