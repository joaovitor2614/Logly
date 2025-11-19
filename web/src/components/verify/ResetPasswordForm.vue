<script setup lang="ts">
import Form from '../auth/Form.vue';

import useForm from '@/hooks/useForm';
import { useUserStore } from '@/stores';
import { useRoute } from 'vue-router';

interface Props {
    userEmail: string,
    otpCode: string
}

const props = defineProps<Props>();

const { form, errorsMessages, formFieldsInvalidState } = useForm()
const userStore = useUserStore()




const handlResetPassword = async () => {

  
    await userStore.tryResetPassword(form.password, props.userEmail, props.otpCode);
  
}
</script>

<template>

        <form @submit.prevent="handlResetPassword">
         <Form :form="form" :errorsMessages="errorsMessages" :authType="'reset-password'"/>
         <div class="text-center">
            <Button :buttonAction="handlResetPassword">Change password</Button>
        </div>
        </form>



</template>

<style lang="scss" scoped>

</style>