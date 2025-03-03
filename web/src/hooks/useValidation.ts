import { ref, onMounted, onUnmounted, computed, type Reactive } from 'vue'
import { required, email, sameAs } from '@vuelidate/validators'
import { useVuelidate } from '@vuelidate/core'


interface Form {
    username?: string,
    email: string,
    password: string,
    confirmPassword?: string
}


const useValidation = (form: Reactive<Form>, authType: 'login' | 'register' = 'register') => {
    let baseRules = {
        email: { required, email, $autoDirty: true },
        password: { required,  $autoDirty: true },
    };
   
    if (authType === 'register') {
        const registerRules = {
            username: { required,  $autoDirty: true },
            confirmPassword: sameAs(form.password)
        }
        baseRules = {
            ...registerRules
        }

    }

    const v$ = useVuelidate(baseRules, form);

    function createFormAttributeErrors(attributeName: string) {
        const errors = []
        if (!v$.value[attributeName]) return errors
    
        if (v$.value[attributeName].$error) {
            for (const error in v$.value[attributeName].$errors) {
                errors.push(error.$message)
            }
        }
        console.log(errors)
        return errors
    }




    const userNameErrors = computed(() => {
        return createFormAttributeErrors('username')
    });
    const emailErrors = computed(() => {
        return createFormAttributeErrors('email')
    })
    const passwordErrors = computed(() => {
        return createFormAttributeErrors('password')
    });
    const errors = { 'username': userNameErrors.value, 'email': emailErrors.value, 'password': passwordErrors.value};
    const isDisabled = computed(() =>  authType == 'register' ? 
    v$.value.username.$invalid || v$.value.email.$invalid || v$.value.password.$invalid
    : v$.value.email.$invalid || v$.value.password.$invalid);

    return {
        errors,
        isDisabled
    }

}

export default useValidation