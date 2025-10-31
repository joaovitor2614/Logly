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

export async function deleteCurrentUserAccount() {
    return api.delete(`/users`)
    
}


export const sendEmailVerificationCode = () => {
    return api.post(`users/send-verification-code/`);
}

export const sendResetPasswordLink = (email: string) => {
    return api.post(`users/send-reset-password-code/`, {"email": email});
}

export const resetPassword = (newPassword: string, resetPasswordToken: string) => {
    return api.post(`users/reset-password-link/${resetPasswordToken}`, {"password": newPassword});
}



export const verifyEmailVerificationCode = (code: string) => {
    return api.put(`users/verify-verification-code/${code}`);
}