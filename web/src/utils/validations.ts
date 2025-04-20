import { type Ref } from 'vue'

/**
 * Given a form attribute and a Vuelidate computed object, returns an array
 * of error messages for the given attribute.
 * @param v$ - the Vuelidate computed object
 * @param attributeName - the name of the form attribute
 * @returns an array of error messages
 */
export function createFormAttributeErrors(v$: Ref <any>, attributeName: string) {
    const errors = []
 
    if (v$.value[attributeName].$errors) {
        v$.value[attributeName].$errors.forEach((error) => {
            errors.push(error.$message)
        })
    }
    
    return errors
}