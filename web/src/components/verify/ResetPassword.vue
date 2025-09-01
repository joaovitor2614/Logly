<script setup>
import Form from '../auth/Form.vue';
import AuthBase from '../auth/AuthBase.vue'
import useForm from '@/hooks/useForm';


const { form, errorsMessages, formFieldsInvalidState } = useForm()

const handlResetPassword = () => {
    console.log('handlResetPassword')
}
</script>

<template>
    <AuthBase :helperTitle="'Reset your password'">
        <form @submit.prevent="handlResetPassword">
         <Form :form="form" :errorsMessages="errorsMessages" :authType="'reset-password'"/>
         <div class="text-center">
            <Button :buttonAction="redirectToLogin" :id="'test-redirect-to-login-btn'">Change password</Button>
        </div>
        </form>


    </AuthBase>
</template>

<style lang="scss" scoped>

</style>