import api from "../api";



export async function getUserInfo(): Promise<{ userInfo: App.User.Info, hasErrors: boolean }> {
    const { data, hasErrors }  = await api.get<App.User.Info>('users')
    return { userInfo: data, hasErrors }
}

export async function putUserInfo(userID: string, userData: Partial<App.User.Info>): Promise<{ updatedUserInfo: App.User.Info, hasErrors: boolean }> {
    const { data, hasErrors } = await api.put<App.User.Info>(`users/${userID}`, userData)
    return { updatedUserInfo: data, hasErrors }
}


