import { type Ref } from 'vue'
import { helpers } from '@vuelidate/validators'
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



/**
 * Creates a validator that checks if a value compares to another value in a
 * certain way, as specified by the compareFn function. The other value is
 * determined by the getOtherField function, which is passed the parent object
 * of the value being validated. If either value is null, the validation passes
 * without checking the comparison. The message parameter is used as the error
 * message if the comparison fails.
 *
 * @param compareFn - A function that takes two values and returns true if they
 *   meet the comparison criteria, and false otherwise.
 * @param getOtherField - A function that takes the parent object of the value
 *   being validated and returns the other value to compare against.
 * @param message - The error message to display if the comparison fails.
 */
function createComparisonValidator<TParent, TValue>(
  compareFn: (a: TValue, b: TValue) => boolean,
  getOtherField: (parent: TParent) => TValue | null | undefined,
  message: string
) {
  return helpers.withMessage(
    message,
    helpers.withParams({}, (value: TValue | null | undefined, parent: TParent) => {
      const other = getOtherField(parent)
      if (value == null || other == null) return true
      return compareFn(value, other)
    })
  )
}

export const topLessThanOrEqualBottom = createComparisonValidator<
  { top: number; bottom: number },
  number
>(
  (top, bottom) => top < bottom,
  (parent) => parent?.bottom,
  'Must be less than bottom'
)

export const bottomGreaterThanOrEqualTop = createComparisonValidator<
  { top: number; bottom: number },
  number
>(
  (bottom, top) => bottom > top,
  (parent) => parent?.top,
  'Must be greater than top'
)