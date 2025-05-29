import useVuelidate from '@vuelidate/core';

import { computed, ComputedRef, Reactive, reactive } from 'vue';
import { createFormAttributeErrors } from '../utils/validations';
import { baseForm, baseRules } from './base'



const useForm = () => {

      const form = reactive(baseForm)
  


      const v$ = useVuelidate(baseRules, form);

      function createFormFieldsByAttribute<T>(
        formFieldMapper: (formField: string) => T
      ): Record<string, T> {
        return Object.fromEntries(
          Object.keys(baseRules).map((formField) => [formField, formFieldMapper(formField)])
        );
      }

      const errorsMessages: ComputedRef<Record<keyof typeof baseRules, string[]>> = computed(() => 
          createFormFieldsByAttribute((formField) => createFormAttributeErrors(v$, formField))
      )
      const formFieldsInvalidState: ComputedRef<Record<keyof typeof baseRules, boolean>> = computed(() => 
          createFormFieldsByAttribute((formField) => v$.value[formField].$invalid)
      )
  

      return { form, errorsMessages, formFieldsInvalidState }
}

export default useForm