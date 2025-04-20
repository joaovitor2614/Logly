import useVuelidate from '@vuelidate/core';
import { required, email, sameAs } from '@vuelidate/validators'
import { computed, ComputedRef, Reactive, reactive } from 'vue';
import { createFormAttributeErrors } from '../utils/validations';



const useForm = () => {
    const formInitialValues = {
        name: '',
        email: '',
        password: '',
        confirmPassword: '',
        disciplines: [],
        gender: 'other',
        phone: '',
        image: ''
    }
    const form = reactive(formInitialValues)
  
    const formRules = {
        name: { required,  $autoDirty: true },
        email: { required, email, $autoDirty: true },
        password: { required,  $autoDirty: true },
        confirmPassword: sameAs(form.password),
        disciplines: { required,  $autoDirty: true },
      };

      const v$ = useVuelidate(formRules, form);
      const errorsMessages: ComputedRef<Record<keyof typeof formRules, string[]>> = computed(() => Object.fromEntries(
        Object.keys(formRules).map((formAttribute) => {
          return [formAttribute, createFormAttributeErrors(v$, formAttribute)]
        
        }))
      )
      console.log('errorsMessages', errorsMessages)

      return { form, errorsMessages }
}

export default useForm