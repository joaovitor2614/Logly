import api from "../api";


export async function getUserInfo() {
    return api.get<App.User.Info>('users')
}

export async function getUserInfoByID(id: string) {
    return api.get<App.User.Info>(`/users/${id}`)
    
}

export async function putUserInfo(userID: string, userData: Partial<App.User.Info>) {
    return api.put<App.User.Info>(`users/${userID}`, userData)
    
}


