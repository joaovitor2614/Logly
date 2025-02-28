import api from './api'

export const setAPIHeadersAuthToken = (token: string): void => {
    api.defaults.headers.common['x-auth-token'] = token
}


export const deleteAPIHeadersAuthToken = (): void =>  {
    delete api.defaults.headers.common['x-auth-token'] 
}
