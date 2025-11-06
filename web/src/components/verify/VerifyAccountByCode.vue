<script setup lang="ts">
import OTPCode from './OTPCode.vue';
import { sendEmailVerificationCode} from '@/api/services/user';
import { getMaskedEmail } from '@/utils/email'
import { onMounted } from 'vue';
import { Ref, ref } from 'vue';
import { computed } from 'vue';
import { useToast } from 'vue-toastification';
import { useUserStore } from '@/stores';
const toast = useToast();

const userStore = useUserStore();
const maskedUserEmail: Ref<string> = ref(getMaskedEmail(userStore.userInfo.email));
const otpCode: Ref<string> = ref('')
const isLoadingSendCode: Ref<boolean> = ref(false);
const isLoadingVerify: Ref<boolean> = ref(false);






const isVerifyAccountDisabled = computed(() => {
    const hasNotEnteredCode = otpCode.value.replace(/\s/g, '').length === 6 ? false : true;
    return hasNotEnteredCode || isLoadingSendCode.value
})

const sendOTPCodeToUserEmail = async () => {
    isLoadingSendCode.value = true
    otpCode.value = '';
    const response = await sendEmailVerificationCode();
    if (response) {
        toast.success('Verification code sent successfully!')
    }
    isLoadingSendCode.value = false
}

const verifyOTPCode = async ()  => {
    isLoadingVerify.value = true
    userStore.verifyPassedOTPCode(otpCode.value)
    isLoadingVerify.value = false
}


onMounted(() => {
    sendOTPCodeToUserEmail()
})


</script>

<template>

    <div class="relative flex min-h-screen flex-col justify-center overflow-hidden bg-gray-50 py-12">
        <div class="relative bg-white px-6 pt-10 pb-9 shadow-xl mx-auto w-full max-w-lg rounded-2xl">
            <div class="mx-auto flex w-full max-w-md flex-col space-y-16">
            <div class="flex flex-col items-center justify-center text-center space-y-2">
                <div class="font-semibold text-3xl">
                <p>Email Verification</p>
                </div>
                <div class="flex flex-row text-sm font-medium text-gray-400">
                <p>We have sent a code to your email {{ maskedUserEmail }}</p>
                </div>
            </div>
            <OTPCode
                v-model:otpCode="otpCode" 
                :isVerifyAccountDisabled="isVerifyAccountDisabled" 
                :sendOTPCode="sendOTPCodeToUserEmail"
                :isLoadingVerify="isLoadingVerify"
                :verifyFunction="verifyOTPCode"
            />
            
     
            </div>
            </div>
        </div>
    
</template>

<style scoped>

</style>