
import { required, email, sameAs } from '@vuelidate/validators'
export function createBaseForm() {
        return {
                name: '',
                email: '',
                password: '',
                confirmPassword: '',
        }
}

export const baseRules = {
        name: { required,  $autoDirty: true },
        email: { required, email, $autoDirty: true },
        password: { required,  $autoDirty: true },
};