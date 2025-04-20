<script setup lang="ts">

import { computed } from 'vue';
import { useAuthStore } from '../../stores/index';

import useForm from '../../hooks/useForm'
import { router } from '../../router/router'
import AuthBase from './AuthBase.vue'








</script>

<template>
    
    
    <AuthBase :helperTitle="'Create an account to start using it..'">
        <form>
                <v-text-field

                    name="username"
                    label="Username"
                    type="text"
                    placeholder="username"
         
                    required
                ></v-text-field>
                <v-text-field
                    name="email"
                    label="Email Address"
                    type="email"
                    placeholder="email"
         
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