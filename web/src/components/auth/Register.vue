<script setup lang="ts">
import { reactive } from 'vue';

interface Form {
    username: string,
    password: string,
    confirmPassword: string,
}

const form = reactive({
    username: '',
    password: '',
    confirmPassword: ''
})
    form

const handleRegister = () => {
    console.log('handleRegister', handleRegister)
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
                                name="username"
                                label="Username"
                                type="text"
                                placeholder="username"
                                required
                            ></v-text-field>
                            <v-text-field
                                name="password"
                                label="Password"
                                type="password"
                                placeholder="password"
                                required
                            ></v-text-field>
                            <v-text-field 
                                name="confirmPassword"
                                label="Confirm Password"
                                type="password"
                                placeholder="cocnfirm password"
                                required
                            ></v-text-field>
                            <div class="red--text"> Error Message</div>
                            <v-btn type="submit" class="mt-4" color="primary" value="log in">Register</v-btn>
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