import api from "../api";


export const sendEmailVerificationCode = (userID: string) => {
    return api.get(`/verify-email/${userID}`);
}


export const checkEmailVerificationCode = (userID: string, verifyAccountCode: number) => {
    return api.post(`/verify-email/${userID}`, { code: verifyAccountCode});
}