<script setup lang="ts">
import { reactive, computed } from 'vue';
import { useAuthStore } from '../../stores/auth';
import { required, email, sameAs } from '@vuelidate/validators'
import useVuelidate from '@vuelidate/core';
import { createFormAttributeErrors} from '../../utils/validations'

interface Form {
    email: string,
    password: string,
}

const form = reactive({
    email: '',
    password: '',
})

const rules = {
  email: { required, email, $autoDirty: true },
  password: { required,  $autoDirty: true },
};

const v$ = useVuelidate(rules, form);

const isDisabled = computed (() =>   v$.value.email.$invalid || v$.value.password.$invalid);



const emailErrors = computed(() => createFormAttributeErrors(v$, 'email'))
const passwordErrors = computed(() => createFormAttributeErrors(v$, 'password'))

const authStore = useAuthStore();

const handleLogin = async () => {
    const response = await authStore.loginUser({ password: form.password, email: form.email });

}
</script>

<template>
    
    
           
        <div class="d-flex justify-center">
            <v-card class="elevation-12" width="50vh">
                        <v-toolbar dark color="primary">
                            <v-toolbar-title>Login form</v-toolbar-title>
                        </v-toolbar>
                        <v-card-text>
                        <form @submit.prevent="handleLogin">
                            <v-text-field
                                v-model="form.email"
                                name="email"
                                label="Email"
                                type="email"
                                placeholder="email"
                                :error-messages="emailErrors"
                                required
                            ></v-text-field>
                            <v-text-field
                                v-model="form.password"
                                name="password"
                                label="Password"
                                type="password"
                                placeholder="password"
                                :error-messages="passwordErrors"
                                required
                            ></v-text-field>
                            <v-btn type="submit" class="mt-4" color="primary" value="log in" :disabled="isDisabled">Login</v-btn>
                        

                        </form>

                        </v-card-text>
                    </v-card>
        </div>
                   
               
            
       

</template>

<style scoped>


</style>