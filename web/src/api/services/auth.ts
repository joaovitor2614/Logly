import api from "../api";


export async function authenticateUser(authType: 'register' | 'login', userData: App.User.Register | App.User.Login): Promise<{ jwtToken: string, hasErrors: boolean }> {
    const { data, hasErrors } = await api.post<App.Auth.Token>(`auth/${authType}`, userData);
    
    return { jwtToken: data.token, hasErrors }
}
