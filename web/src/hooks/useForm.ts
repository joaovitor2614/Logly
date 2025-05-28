import useVuelidate from '@vuelidate/core';

import { computed, ComputedRef, Reactive, reactive } from 'vue';
import { createFormAttributeErrors } from '../utils/validations';
import { baseForm, baseRules } from './base'



const useForm = () => {

      const form = reactive(baseForm)
  


      const v$ = useVuelidate(baseRules, form);

      const errorsMessages: ComputedRef<Record<keyof typeof baseRules, string[]>> = computed(() => Object.fromEntries(
        Object.keys(baseRules).map((formAttribute) => {
          return [formAttribute, createFormAttributeErrors(v$, formAttribute)]
        
        }))
      )

      const formFieldsInvalidState: ComputedRef<Record<keyof typeof baseRules, boolean>> = computed(() => Object.fromEntries(
        Object.keys(baseRules).map((formAttribute) => {
          return [formAttribute, v$.value[formAttribute].$invalid]
        
        }))
      )
  

      return { form, errorsMessages, formFieldsInvalidState }
}

export default useForm