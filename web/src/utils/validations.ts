import { type Ref } from 'vue'

/*************  ✨ Codeium Command ⭐  *************/
/**
 * Given a form attribute and a Vuelidate computed object, returns an array
 * of error messages for the given attribute.
 * @param v$ - the Vuelidate computed object
 * @param attributeName - the name of the form attribute
 * @returns an array of error messages
 */
/******  c238d53c-c9d5-4c81-a2f2-9b7635affd3e  *******/
export function createFormAttributeErrors(v$: Ref<any>, attributeName: string) {
    const errors = []
    v$.value[attributeName].$errors.forEach((error) => {
            errors.push(error.$message)
    })
    return errors
}