

export interface LoginForm {
    email: string,
    password: string,
}


export interface RegisterForm extends LoginForm {
    password: string,
    confirmPassword: string
}