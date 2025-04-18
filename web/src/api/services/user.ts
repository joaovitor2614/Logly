import api from "../api";



export async function getUserInfo(): Promise<Api.User.Info> {
    const response = await api.get<Api.User.Info>('users')
    return response
}

export async function putUserInfo(): Promise<Api.User.Info> {
    const response = await api.put<Api.User.Info>('users')
    return response
}


