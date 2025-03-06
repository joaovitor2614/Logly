declare namespace App {
    namespace User {
        interface Login {
            password: string,
            email: string
        }
    
        interface Register extends Login {
            confirmPassword: string,
            username: string
        }
    }
    type GenderType = 'male' | 'female'
    interface Professor {
        name: string,
        image: string,
        disciplines: string[],
        gender: GenderType,
        phone: string,
        upvotes: string,
        downvotes: string
    }
}