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
            image: string,
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
            company: string
            start: number
            stop: number
            create_time: string
            welllogs: WellLog[]
        }

        interface WellLog {
            _id: string
            name: string
            unit: string
            min_value: Number,
            max_value: Number,
            description: string
            data: number[]
        }
    }

    namespace Plot {
        interface AxisTemplate {
            id: string,
            range: [Number, Number] | [],
            data: number[] | [],
            unit: string,
            name: string,
        }
        interface Axes {
            x: AxisTemplate,
            y: AxisTemplate
        }
        interface Template {
            type: 'histogram' | 'scatter',
            wellID: string,
            color: string,
            axes: Axes,
            hasTemplateChanged: boolean
        }

    }






    
}