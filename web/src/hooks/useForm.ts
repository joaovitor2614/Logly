import useVuelidate from '@vuelidate/core';
import { required, email, sameAs } from '@vuelidate/validators'
import { computed, Reactive, reactive } from 'vue';
import { createFormAttributeErrors } from '../utils/validations';

const useForm = () => {
    const formInitialValues = {
        username: '',
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
        username: { required,  $autoDirty: true },
        email: { required, email, $autoDirty: true },
        password: { required,  $autoDirty: true },
        confirmPassword: sameAs(form.password),
        disciplines: { required,  $autoDirty: true },
      };
      
      const v$ = useVuelidate(formRules, form);
      const errorsMessages = computed(() => Object.keys(formRules).map((formAttribute) => {
        console.log('formAttribute', formAttribute)
        return {
            formAttribute: createFormAttributeErrors(v$, formAttribute)
        }
      }));


      return { form, errorsMessages }
}

export default useForm