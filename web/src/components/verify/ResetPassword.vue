<script setup>
import Form from '../auth/Form.vue';
import AuthBase from '../auth/AuthBase.vue'
import useForm from '@/hooks/useForm';
import { useUserStore } from '@/stores';
import { useRoute } from 'vue-router';


const { form, errorsMessages, formFieldsInvalidState } = useForm()
const userStore = useUserStore()
const route = useRoute()

const handlResetPassword = async () => {
    const resetPasswordToken = route.params.token
    await userStore.tryResetPassword(form.password, resetPasswordToken);
  
}
</script>

<template>
    <AuthBase :helperTitle="'Reset your password'">
        <form @submit.prevent="handlResetPassword">
         <Form :form="form" :errorsMessages="errorsMessages" :authType="'reset-password'"/>
         <div class="text-center">
            <Button :buttonAction="handlResetPassword">Change password</Button>
        </div>
        </form>


    </AuthBase>
</template>

<style lang="scss" scoped>

</style>