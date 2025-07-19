import useVuelidate from '@vuelidate/core';

import { computed, ComputedRef, Reactive, reactive } from 'vue';
import { createFormAttributeErrors } from '../utils/validations';
import { createBaseForm, baseRules } from './base'



const useForm = () => {


      const form = reactive(createBaseForm())
  
      const rules = baseRules(form)

      const v$ = useVuelidate(rules, form);

      function createFormFieldsByAttribute<T>(
        formFieldMapper: (formField: string) => T
      ): Record<string, T> {
        return Object.fromEntries(
          Object.keys(rules).map((formField) => [formField, formFieldMapper(formField)])
        );
      }

      const errorsMessages: ComputedRef<Record<keyof typeof rules, string[]>> = computed(() => 
          createFormFieldsByAttribute((formField) => createFormAttributeErrors(v$, formField))
      )
      const formFieldsInvalidState: ComputedRef<Record<keyof typeof rules, boolean>> = computed(() => 
          createFormFieldsByAttribute((formField) => v$.value[formField].$invalid)
      )
  

      return { form, errorsMessages, formFieldsInvalidState }
}

export default useForm