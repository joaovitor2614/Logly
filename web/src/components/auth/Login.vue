<script setup lang="ts">
import { reactive, computed, type Reactive } from 'vue';
import { useAuthStore } from '../../stores/index';
import { required, email, sameAs } from '@vuelidate/validators'
import useVuelidate from '@vuelidate/core';
import { createFormAttributeErrors} from '../../utils/validations'
import { router } from '../../router/router'

const form: Reactive<App.User.Login> = reactive({
    email: '',
    password: '',
})

const rules = {
  email: { required, email, $autoDirty: true },
  password: { required,  $autoDirty: true },
};

const v$ = useVuelidate(rules, form);

const isDisabled = computed (() =>   v$.value.email.$invalid || v$.value.password.$invalid);



const emailErrors = computed(() => createFormAttributeErrors(v$, 'email'))
const passwordErrors = computed(() => createFormAttributeErrors(v$, 'password'))

const authStore = useAuthStore();

const handleLogin = async () => {
    await authStore.loginUser({ password: form.password, email: form.email });

}
</script>

<template>
    
    
           
        <v-container>
            <v-row align="center" justify="center">
                <v-col cols="12" sm="10">
                    <v-card>
                        <v-toolbar dark color="primary">
                            <v-toolbar-title>Login form</v-toolbar-title>
                        </v-toolbar>
                        <v-card-text>
                        <form @submit.prevent="handleLogin">
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

                        </v-card-text>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
                   
               
            
       

</template>

<style scoped>


</style>