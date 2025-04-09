import api from "../api";



export async function getUserInfo(): Promise<Api.User.Info> {
    const response = await api.get<Api.User.Info>('users')
    return response.data
}
