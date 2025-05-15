import api from "../api";
import { ApiResponse } from './types'

export async function getUserInfo(): Promise<ApiResponse<App.User.Info>> {
    return api.get<App.User.Info>('users')
}

export async function getUserInfoByID(id: string): Promise<ApiResponse<App.User.Info>> {
    return api.get<App.User.Info>(`/users/${id}`)
    
}

export async function putUserInfo(userID: string, userData: Partial<App.User.Info>): Promise<ApiResponse<App.User.Info>> {
    return api.put<App.User.Info>(`users/${userID}`, userData)
    
}


