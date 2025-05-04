import useVuelidate from '@vuelidate/core';
import { required, email, sameAs } from '@vuelidate/validators'
import { computed, ComputedRef, Reactive, reactive } from 'vue';
import { createFormAttributeErrors } from '../utils/validations';
import { hasArrayAtLeastOneItem, isValidPhoneNumber } from '@/validation';



const useForm = () => {
    const formInitialValues = {
        name: '',
        email: '',
        password: '',
        confirmPassword: '',
        disciplines: [],
        gender: 'other' as App.Professor.Gender,
        phone: '',
        image: ''
    }
    const form = reactive(formInitialValues)
  
    const formRules = {
        name: { required,  $autoDirty: true },
        email: { required, email, $autoDirty: true },
        password: { required,  $autoDirty: true },
        confirmPassword: sameAs(form.password),
        phone: { required,  isValidPhoneNumber, $autoDirty: true },
        disciplines: { hasArrayAtLeastOneItem,  $autoDirty: true },
      };

      const v$ = useVuelidate(formRules, form);

      const errorsMessages: ComputedRef<Record<keyof typeof formRules, string[]>> = computed(() => Object.fromEntries(
        Object.keys(formRules).map((formAttribute) => {
          return [formAttribute, createFormAttributeErrors(v$, formAttribute)]
        
        }))
      )

      const formFieldsInvalidState: ComputedRef<Record<keyof typeof formRules, boolean>> = computed(() => Object.fromEntries(
        Object.keys(formRules).map((formAttribute) => {
          return [formAttribute, v$.value[formAttribute].$invalid]
        
        }))
      )
  

      return { form, errorsMessages, formFieldsInvalidState }
}

export default useForm