<script setup lang="ts">
import AuthBase from '../auth/AuthBase.vue';
import { sendResetPasswordCode, verifyResetPasswordCode } from '@/api/services/user';
import Button from '@/components/common/Button.vue'
import { Ref, ref, computed } from 'vue';
import { useToast } from 'vue-toastification';
import OTPCode from './OTPCode.vue';
import ResetPasswordForm from './ResetPasswordForm.vue';
import useForm from '@/hooks/useForm';


const { form, errorsMessages, formFieldsInvalidState } = useForm()


const otpCode: Ref<string> = ref('')
const helperTitle: Ref<string> = ref('Send reset password link')
const isLoadingSendResetPasswordCode: Ref<boolean> = ref(false);
const isLoadingVerifyResetPasswordCode: Ref<boolean> = ref(false);
const hasSentResetPasswordCode: Ref<boolean> = ref(false);
const hasVerifiedResetPasswordCode: Ref<boolean> = ref(false);
const toast = useToast()
const executeSendResetPasswordCode = async () => {
    isLoadingSendResetPasswordCode.value = true
    const response = await  sendResetPasswordCode(form.email)
    if (response) {
        helperTitle.value = "Enter sent OTP code"
        toast.success('Password reset code sent successfully!')
        hasSentResetPasswordCode.value = true

    }
    isLoadingSendResetPasswordCode.value = false
}
const executeVerifyResetPasswordCode = async () => {
    console.log('executeVerifyResetPasswordCode')
    const response = await verifyResetPasswordCode(form.email, otpCode.value)
    if (response) {
        helperTitle.value = "Enter new password"
        hasVerifiedResetPasswordCode.value = true
    }
}
const isDisabled = computed(() => formFieldsInvalidState.value['email']);
const isResetPasswordDisabled = computed(() => {
    const hasNotEnteredCode = otpCode.value.replace(/\s/g, '').length === 6 ? false : true;
    return hasNotEnteredCode || !otpCode.value
})


</script>

<template>
    <AuthBase :helperTitle="helperTitle">
        <form v-if="!hasSentResetPasswordCode">
            <v-text-field
                name="email"
                label="Email Address"
                type="email"
                :error-messages="errorsMessages.email"
                v-model="form.email"
                placeholder="email"
                class="mt-5 mb-6"
            />
             <div class="d-flex justify-center align-center">
            <Button 
                :buttonAction="executeSendResetPasswordCode" 
                :isDisabled="isDisabled"
                :isButtonLoading="isLoadingSendResetPasswordCode"


                >
                Send
            </Button>
             </div>
    
        </form>

        <div v-if="hasSentResetPasswordCode && !hasVerifiedResetPasswordCode">
            <OTPCode
                v-model:otpCode="otpCode" 
                :verifyFunction="executeVerifyResetPasswordCode"
                :isLoadingVerify="isLoadingVerifyResetPasswordCode"
                :isDisabled="isResetPasswordDisabled" 
                :sendOTPCode="executeSendResetPasswordCode"
            />
        </div>
        <div v-if ="hasVerifiedResetPasswordCode">
            <ResetPasswordForm :otpCode="otpCode" :userEmail="form.email"/>
        </div>

    </AuthBase>


</template>

<style lang="scss" scoped>

</style>