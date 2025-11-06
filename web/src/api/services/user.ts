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

export const sendResetPasswordCode = (email: string) => {
    return api.post(`users/send-reset-password-code/`, {"email": email});
}

export const resetPassword = (newPassword: string, userEmail: string, otpCode: string) => {
    return api.post(`users/reset-password`, {"password": newPassword, "otp_code": otpCode, "email": userEmail});
}



export const verifyEmailVerificationCode = (code: string, verificationType: string) => {
    
    return api.put(`users/verify-account-verification-code/${code}`);
}

export const verifyResetPasswordCode = (userEmail: string, otpCode: string) => {
    
    return api.put(`users/verify-reset-password-code/`, {"otp_code": otpCode, "email": userEmail});
}

