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
            has_confirmed_email: boolean,
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

    namespace Well {
        interface Well {
             _id: string
            name: string
            create_time: string
            welllogs: WellLog[]
        }

        interface WellLog {
            _id: string
            mnemonic: string
            unit: string
            description: string
            data: number[]
        }
    }





    
}