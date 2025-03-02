<script setup lang="ts">
import { reactive } from 'vue';import useVuelidate from '@vuelidate/core';
import { useAuthStore } from '../../stores/auth';
import useValidation from '../../hooks/useValidation'

interface Form {
    username: string,
    password: string,
}

const form = reactive({
    username: '',
    password: '',
})

const { errors, isDisabled } = useValidation(form)

const authStore = useAuthStore();

const handleLogin = () => {
    authStore.registerUser({ password: form.password, email: form.email })
   
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
                                v-model="form.username"
                                name="username"
                                label="Username"
                                type="text"
                                placeholder="username"
                                :error-messages="errors.username"
                                required
                            ></v-text-field>
                            <v-text-field
                                v-model="form.email"
                                name="password"
                                label="Password"
                                type="password"
                                :error-messages="errors.email"
                                placeholder="password"
                                required
                            ></v-text-field>
                            <div class="red--text"> Error Message</div>
                            <v-btn type="submit" class="mt-4" color="primary" value="log in">Login</v-btn>
                            <div class="grey--text mt-4">
                                w 
                            </div>

                        </form>

                        </v-card-text>
                    </v-card>
        </div>
                   
               
            
       

</template>

<style scoped>


</style>