<script setup lang="ts">
import { reactive } from 'vue';

interface Form {
    username: string,
    password: string,
}

const form = reactive({
    username: '',
    password: '',
})


const handleLogin = () => {
    console.log('handleLogin', handleLogin)
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