import api from './api'

export const setAPIHeadersBearerToken = (token: string): void => {
    api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}


export const deleteAPIHeadersAuthToken = (): void =>  {
    delete api.defaults.headers.common['Authorization']
}
