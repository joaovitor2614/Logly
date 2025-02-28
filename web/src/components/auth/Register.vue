<script setup lang="ts">
import { reactive, computed } from 'vue';
import { useAuthStore } from '../../stores/auth';
import { type Reactive } from 'vue';
import useVuelidate from '@vuelidate/core';
import { required, email, sameAs } from '@vuelidate/validators'


interface Form {
    username: string;
    email: string;
    password: string;
    confirmPassword: string;
}

const form: Reactive<Form> = reactive({
    username: '',
    email: '',
    password: '',
    confirmPassword: ''
})



const rules = {
  username: { required,  $autoDirty: true },
  email: { required, email, $autoDirty: true },
  password: { required,  $autoDirty: true },
  confirmPassword: sameAs(form.password)
};

const v$ = useVuelidate(rules, form);

const isDisabled = computed (() =>  v$.value.username.$invalid || v$.value.email.$invalid || 
v$.value.password.$invalid || v$.value.confirmPassword.$invalid);

const userNameErrors = computed(() => {
    const errors = []

    if (v$.value.username.required && v$.value.username.$error) {
    errors.push('User name is required')
    }
    return errors
});
const emailErrors = computed(() => {
    const errors = []

    if (v$.value.email.$error) {
    errors.push('Valid email is required')
    }
    return errors
})

const passwordErrors = computed(() => {
    const errors = []

    if (v$.value.password.$error) {
    errors.push('Password is required')
    }
    return errors
})

const authStore = useAuthStore();


const handleRegister = () => {
    authStore.registerUser({ name: form.username, password: form.password, email: form.email })
    console.log('handleRegister')
}
</script>

<template>
    
    
           
        <div class="d-flex justify-center">
            <v-card class="elevation-12" width="50vh">
                        <v-toolbar dark color="primary">
                            <v-toolbar-title>Register form</v-toolbar-title>
                        </v-toolbar>
                        <v-card-text>
                        <form @submit.prevent="handleRegister">
                            <v-text-field
                                v-model="form.username"
                                name="username"
                                label="Username"
                                type="text"
                                placeholder="username"
                                :error-messages="userNameErrors"
                                required
                            ></v-text-field>
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
                            <v-text-field 
                                v-model="form.confirmPassword"
                                name="confirmPassword"
                                label="Confirm Password"
                                type="password"
                                placeholder="cocnfirm password"
                                required
                            ></v-text-field>

                            <v-btn :disabled="isDisabled" type="submit" class="mt-4" color="primary" value="log in">Register</v-btn>
                        </form>

                        </v-card-text>
                    </v-card>
        </div>
                   
               
            
       

</template>

<style scoped>


</style>