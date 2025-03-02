
import axios from 'axios'

const api = axios.create({
    baseURL: 'http://127.0.0.1:5000',
    timeout: 1000,
    headers: {'X-Custom-Header': 'foobar'}
});



export default api
