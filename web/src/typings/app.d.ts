declare namespace App {
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
    namespace User {
        interface Login {
            password: string,
            email: string
        }
    
        interface Register extends Login {
            name: string
        }
    }





    
}