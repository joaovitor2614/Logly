<script setup lang="ts">

import { computed } from 'vue';
import { useAuthStore } from '../../stores/index';

import useForm from '../../hooks/useForm'
import { router } from '../../router/router'
import AuthBase from './AuthBase.vue'



const { form, errorsMessages } = useForm()

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
                    :error-messages="errorsMessages.username"
                    name="username"
                    label="Username"
                    type="text"
                    placeholder="username"
         
                    required
                ></v-text-field>
                <v-text-field
                    v-model="form.email"
                    :error-messages="errorsMessages.email"
                    name="email"
                    label="Email Address"
                    type="email"
                    placeholder="email"
         
                    required
                ></v-text-field>
                <v-text-field
                    v-model="form.password"
                    :error-messages="errorsMessages.password"
                    name="password"
                    label="Password"
                    type="password"
        
                    placeholder="password"
                    required
                ></v-text-field>
                <v-text-field 
                    v-model="form.confirmPassword"
                    :error-messages="errorsMessages.confirmPassword"
                    name="confirmPassword"
                    label="Confirm Password"
                    type="password"
                    placeholder="cocnfirm password"
          
                    required
                ></v-text-field>
                
                <v-btn type="submit" class="mt-4" color="primary" value="log in" :disabled="false">Register</v-btn>
                <div style="  text-align: center; padding: 10px 0;">
                        <v-card-text class="white--text" >
                            <h3 class="text-center ">Alredy Signed up?</h3>
                            <h6
                            class="text-center"
                            >Log in to your account so you can continue building and<br>  editing your onboarding flows</h6>
                        </v-card-text>
                        <div class="text-center">
                            <v-btn tile color="primary" outlined dark>Log in</v-btn>
                        </div>
                </div>

        </form>
    </AuthBase>

               
            
       

</template>

<style scoped>


</style>