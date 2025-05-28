import { hasArrayAtLeastOneItem, isValidPhoneNumber } from '@/validation'
import { required, email, sameAs } from '@vuelidate/validators'

export const baseForm = {
        name: '',
        email: '',
        password: '',
        confirmPassword: '',
        disciplines: [],
        gender: 'other',
        phone: '',
        image: ''
}

export const baseRules = {
        name: { required,  $autoDirty: true },
        email: { required, email, $autoDirty: true },
        password: { required,  $autoDirty: true },
        phone: { required,  isValidPhoneNumber, $autoDirty: true },
        disciplines: { hasArrayAtLeastOneItem,  $autoDirty: true },
};