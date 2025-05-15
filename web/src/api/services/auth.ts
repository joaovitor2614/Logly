import api from "../api";


export async function authenticateUser(authType: 'register' | 'login', userData: App.User.Register | App.User.Login): Promise<{ jwtToken: string | undefined, hasErrors: boolean }> {
    return api.post<App.Auth.Token>(`auth/${authType}`, userData);
}
