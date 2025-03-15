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
        _id: string,
        name: string,
        image: string,
        disciplines: string[],
        gender: GenderType,
        phone: string,
        upvotes: number,
        downvotes: number
    }
}