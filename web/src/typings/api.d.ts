declare namespace Api {
    namespace Auth {
        interface Token {
            token: string
        }
        
        
    }
    namespace User {
        interface Info {
            _id: string
            name: string
            email: string
            image: string
            password?: string
        }
    }
}