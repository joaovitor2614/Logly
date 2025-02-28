<script setup lang="ts">
import { reactive } from 'vue';
import { useAuthStore } from '../../stores/auth';
import { type Reactive } from 'vue';

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

const authStore = useAuthStore()

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
                                required
                            ></v-text-field>
                            <v-text-field
                                v-model="form.email"
                                name="email"
                                label="Email"
                                type="email"
                                placeholder="email"
                                required
                            ></v-text-field>
                            <v-text-field
                                v-model="form.password"
                                name="password"
                                label="Password"
                                type="password"
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

                            <v-btn type="submit" class="mt-4" color="primary" value="log in">Register</v-btn>
                        </form>

                        </v-card-text>
                    </v-card>
        </div>
                   
               
            
       

</template>

<style scoped>


</style>