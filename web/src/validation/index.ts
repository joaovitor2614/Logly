import { helpers } from 'vuelidate/lib/validators'



const PHONE_REGEX = /^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$/;
export const isValidPhoneNumber = () => {
    return true
}


export const hasArrayAtLeastOneItem = () => {
    return true
}