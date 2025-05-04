<script setup lang="ts">
import Button from '@/components/common/Button.vue'
import Form from './Form.vue'
import { useAuthStore } from '../../stores/index';
import { useRouter } from 'vue-router'
import useForm from '../../hooks/useForm'
import AuthBase from './AuthBase.vue'
import { computed } from 'vue';




const { form, errorsMessages, formFieldsInvalidState } = useForm()

const authStore = useAuthStore();
const isDisabled = computed(() => 
    formFieldsInvalidState.value['email'] 
    || formFieldsInvalidState.value['password'] 
    || formFieldsInvalidState.value['name']
    ? true : false
);


const handleRegister = () => {
    authStore.registerUser({ name: form.name, password: form.password, email: form.email });
}

const router = useRouter()
const redirectToLogin = () => {
    router.push("login")
}
</script>

<template>
    
    
    <AuthBase :helperTitle="'Create an account to start using it..'">
        <form @submit.prevent="handleRegister">
                <Form :form="form" :errorsMessages="errorsMessages" :authType="'register'"/>
                
                <Button :buttonAction="handleRegister" :isDisabled="isDisabled">Register</Button>
                <div style="  text-align: center; padding: 10px 0;">
                        <v-card-text class="white--text" >
                            <h3 class="text-center ">Alredy Signed up?</h3>
                            <h6
                            class="text-center"
                            >Log in to your account so you can continue building and<br>  editing your onboarding flows</h6>
                        </v-card-text>
                        <div class="text-center">
                            <Button :buttonAction="redirectToLogin">Log in</Button>
                        </div>
                </div>

        </form>
    </AuthBase>

               
            
       

</template>

<style scoped>


</style>