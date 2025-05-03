<script setup lang="ts">
import Form from './Form.vue'
import Button from '@/components/common/Button.vue'
import { computed } from 'vue';
import { useAuthStore } from '../../stores/index';
import { useRouter } from 'vue-router'
import useForm from '../../hooks/useForm'
import AuthBase from './AuthBase.vue'




const router = useRouter()



const { form, errorsMessages } = useForm()
const isDisabled = computed (() =>   errorsMessages.value.email.length || errorsMessages.value.password.length ? true : false);


const authStore = useAuthStore();

const handleLogin = async () => {
    await authStore.loginUser({ password: form.password, email: form.email });

}

const redirectToRegister = () => {
    router.push("register")
}
</script>

<template>
    
    
        <AuthBase :helperTitle="'Login to access your acount.'">
            <form @submit.prevent="handleLogin">
                <Form :form="form" :errorsMessages="errorsMessages" :authType="'login'"/>
                        <Button :isDisabled="isDisabled" :buttonAction="handleLogin">Login</Button>
                        <div style="  text-align: center; padding: 60px 0;">
                                <v-card-text class="white--text" >
                                    <h3 class="text-center ">Don't Have an Account Yet?</h3>
                                    <h6
                                    class="text-center"
                                    >Let's get you all set up so you can start creating your your first<br>  onboarding experience</h6>
                                </v-card-text>
                                <div class="text-center">
                                    <Button 
                                    :isDisabled="isDisabled" 
                                    :buttonAction="redirectToRegister"
                                    :id="'test-login-btn'"
                                    >
                                        SIGN UP
                                    </Button>
                                 
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