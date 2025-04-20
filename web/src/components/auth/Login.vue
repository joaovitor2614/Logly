<script setup lang="ts">
import { computed } from 'vue';
import { useAuthStore } from '../../stores/index';


import useForm from '../../hooks/useForm'

import { router } from '../../router/router'
import AuthBase from './AuthBase.vue'








const { form, errorsMessages } = useForm()
const isDisabled = computed (() =>   errorsMessages.value.email.length || errorsMessages.value.password.length ? true : false);


const authStore = useAuthStore();

const handleLogin = async () => {
    await authStore.loginUser({ password: form.password, email: form.email });

}
</script>

<template>
    
    
        <AuthBase :helperTitle="'Login to access your acount.'">
            <form @submit.prevent="handleLogin">
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
                            placeholder="password"
                            :error-messages="errorsMessages.password"
                            required
                        ></v-text-field>
                        <v-btn type="submit" class="mt-4" color="primary" value="log in" :disabled="isDisabled">Login</v-btn>
                        <div style="  text-align: center; padding: 60px 0;">
                                <v-card-text class="white--text" >
                                    <h3 class="text-center ">Don't Have an Account Yet?</h3>
                                    <h6
                                    class="text-center"
                                    >Let's get you all set up so you can start creating your your first<br>  onboarding experience</h6>
                                </v-card-text>
                                <div class="text-center">
                                    <v-btn tile color="primary" outlined dark @click="router.push('/register')">SIGN UP</v-btn>
                                </div>
                        </div>
                    

            </form>

        </AuthBase>

               
            
       

</template>

<style scoped>
.login-card {
  max-width: 800px;
  width: 100%;
  border-radius: 12px;
  overflow: hidden;
}

</style>