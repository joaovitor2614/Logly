<script setup lang="ts">
import AuthBase from '../auth/AuthBase.vue';
import { sendResetPasswordCode, verifyResetPasswordCode } from '@/api/services/user';
import Button from '@/components/common/Button.vue'
import { Ref, ref, computed } from 'vue';
import { useToast } from 'vue-toastification';
import OTPCode from './OTPCode.vue';

const emailAddress: Ref<string> = ref('');
const otpCode: Ref<string> = ref('')
const isLoadingSendResetPasswordCode: Ref<boolean> = ref(false);
const isLoadingVerifyResetPasswordCode: Ref<boolean> = ref(false);
const hasSentResetPasswordCode: Ref<boolean> = ref(false);
const hasVerifiedResetPasswordCode: Ref<boolean> = ref(false);
const toast = useToast()
const executeSendResetPasswordCode = async () => {
    isLoadingSendResetPasswordCode.value = true
    const response = await  sendResetPasswordCode(emailAddress.value)
    if (response) {
        toast.success('Password reset code sent successfully!')
        hasSentResetPasswordCode.value = true
    }
    isLoadingSendResetPasswordCode.value = false
}
const executeVerifyResetPasswordCode = async () => {
    console.log('executeVerifyResetPasswordCode')
    const response = await verifyResetPasswordCode(emailAddress.value, otpCode.value)
    if (response) {
        hasVerifiedResetPasswordCode.value = true
    }
}
const isDisabled = computed(() => emailAddress.value ? false : true);
const isResetPasswordDisabled = computed(() => {
    const hasNotEnteredCode = otpCode.value.replace(/\s/g, '').length === 6 ? false : true;
    return hasNotEnteredCode || !otpCode.value
})
</script>

<template>
    <AuthBase :helperTitle="'Send password reset link'">
        <form v-if="!hasSentResetPasswordCode">
            <v-text-field
                name="email"
                label="Email Address"
                type="email"
                v-model="emailAddress"
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

        <div v-if="hasSentResetPasswordCode">
            <OTPCode
                v-model:otpCode="otpCode" 
                :verifyFunction="executeVerifyResetPasswordCode"
                :isLoadingVerify="isLoadingVerifyResetPasswordCode"
                :isDisabled="isResetPasswordDisabled" 
                :sendOTPCode="executeSendResetPasswordCode"
            />
        </div>

    </AuthBase>


</template>

<style lang="scss" scoped>

</style>