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

    namespace Professor {
        interface UserBoundObject {
            _id: string,
            user_id: string
        }
        interface Comment extends UserBoundObject {
            text: string,
            create_time: string,
        }
        interface Vote extends UserBoundObject{
            
        }
        type Gender = "female" | "male" | "other"
        interface Professor {
            _id?: string,
            name: string,
            image: string,
            disciplines: string[],
            gender: Gender,
            comments: Comment[],
            phone: string,
            upvotes: Vote[],
            downvotes: Vote[],
        }

        type AddProfessor = Pick<Professor, 'name' | 'image'>
            
    }
    



    
}