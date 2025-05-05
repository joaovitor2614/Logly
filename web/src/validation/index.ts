import { helpers, required } from 'vuelidate/lib/validators'



const PHONE_REGEX = /^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$/;
export const isValidPhoneNumber = (value: string) => {
    return PHONE_REGEX.test(value)
}


export const hasArrayAtLeastOneItem = (value: []) => {
    return value.length > 0
}