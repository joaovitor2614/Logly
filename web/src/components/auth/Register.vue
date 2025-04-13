<script setup lang="ts">

import { computed } from 'vue';
import { useAuthStore } from '../../stores/index';

import { useForm} from '../../hooks/useForm'
import { router } from '../../router/router'
import AuthBase from './AuthBase.vue'
;

const isDisabled = computed (() =>  errorsMessages.value.username || errorsMessages.value.password || errorsMessages.value.email);


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
                    name="username"
                    label="Username"
                    type="text"
                    placeholder="username"
                    :error-messages="errorsMessages.username"
                    required
                ></v-text-field>
                <v-text-field
                    v-model="form.email"
                    name="email"
                    label="Email"
                    type="email"
                    placeholder="email"
                    :error-messages="errorsMessages.email"
                    required
                ></v-text-field>
                <v-text-field
                    v-model="form.password"
                    name="password"
                    label="Password"
                    type="password"
                    :error-messages="errorsMessages.password"
                    placeholder="password"
                    required
                ></v-text-field>
                <v-text-field 
                    v-model="errorsMessages.confirmPassword""
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