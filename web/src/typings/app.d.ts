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

    namespace Professor {
        interface Comment {
            text: string,
            author: string,
            create_time: string,
            user_id: string
        }
        interface Vote {
            _id: string,
            user_id: string
        }
        interface Professor {
            _id?: string,
            name: string,
            image: string,
            disciplines: string[],
            comments: Comment[],
            phone: string,
            upvotes: number,
            downvotes: number
        }

        interface AddProfessor {
            name: string,
            image: string,
        }
    }
    



    
}