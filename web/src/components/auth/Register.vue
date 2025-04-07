<script setup lang="ts">
import { Form, Field } from 'vee-validate';
import { reactive, computed } from 'vue';
import { useAuthStore } from '../../stores/index';
import { type Reactive } from 'vue';
import useVuelidate from '@vuelidate/core';
import { required, email, sameAs } from '@vuelidate/validators'
import { createFormAttributeErrors } from '../../utils/validations'
import { router } from '../../router/router'
import AuthBase from './AuthBase.vue'


const form: Reactive<App.User.Register> = reactive({
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
v$.value.password.$invalid);

const userNameErrors = computed(() => createFormAttributeErrors(v$, 'username'))
const emailErrors = computed(() => createFormAttributeErrors(v$, 'email'))
const passwordErrors = computed(() => createFormAttributeErrors(v$, 'password'))

const authStore = useAuthStore();



const handleRegister = async () => {
    await authStore.registerUser({ name: form.username, password: form.password, email: form.email });
    
 
}




</script>

<template>
    
    
    <AuthBase :helperTitle="'Create an account to start using it..'">
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
                    :error-messages="passwordErrors"
                    placeholder="password"
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
                
                <v-btn type="submit" class="mt-4" color="primary" value="log in" :disabled="isDisabled">Register</v-btn>
                <div style="  text-align: center; padding: 10px 0;">
                        <v-card-text class="white--text" >
                            <h3 class="text-center ">Alredy Signed up?</h3>
                            <h6
                            class="text-center"
                            >Log in to your account so you can continue building and<br>  editing your onboarding flows</h6>
                        </v-card-text>
                        <div class="text-center">
                            <v-btn tile color="primary" outlined dark @click="router.push('/login')">Log in</v-btn>
                        </div>
                </div>

        </form>
    </AuthBase>

               
            
       

</template>

<style scoped>


</style>