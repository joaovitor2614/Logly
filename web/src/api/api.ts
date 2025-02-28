
import axios from 'axios'

const api = axios.create({
    baseURL: 'http://127.0.0.1:5000',
    timeout: 1000,
    headers: {'X-Custom-Header': 'foobar'}
});


/**
 * Sets the 'x-auth-token' header of the API client to the given token
 * @param {string} token - The token to be set
 */

export default api
