import { helpers } from '@vuelidate/validators'



export const hasArrayAtLeastOneItem = (value: []) => {
    return value.length > 0
}

export const isEqualToValue = (value: string) => helpers.withParams(
    { type: 'isEqualToValue', value: value },
    (value) => !helpers.req(value) || value.includes(value)
  )