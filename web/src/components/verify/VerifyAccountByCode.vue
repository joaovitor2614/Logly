<script setup lang="ts">
import Button from '@/components/common/Button.vue'
import { sendEmailVerificationCode} from '@/api/services/user';

import { useUserStore } from '@/stores';
import { getMaskedEmail } from '@/utils/email'

import { onMounted } from 'vue';
import { Ref, ref } from 'vue';
import { computed } from 'vue';
const userStore = useUserStore()
const maskedUserEmail: Ref<string> = ref(getMaskedEmail(userStore.userInfo.email));

const otpCode: Ref<string> = ref('')


const isDisabled = computed(() => otpCode.value.replace(/\s/g, '').length === 6 ? false : true);

const verifyOTPCode = async ()  => {

    userStore.verifyPassedOTPCode(otpCode.value)
}

const sendOTPCodeToUserEmail = () => {
    otpCode.value = '';
    sendEmailVerificationCode();
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

            <div>
         
                <div class="flex flex-col space-y-16">
                    <v-otp-input 
                    v-model="otpCode" 
                    id='test-otp-code-input'
                    length="6" 
                    type="text" 
                    />
                    <div class="flex flex-col space-y-5">
                    <div>
                    <div class="flex flex-col items-center justify-center mb-4">
                        <Button 
                        :buttonAction="verifyOTPCode" 
                        :is-disabled="isDisabled"
                        :id="'test-verify-otp-btn'"
                        >
                        Verify Account
                        </Button>
                    </div>
             
                    </div>

                    <div class="flex flex-row items-center justify-center text-center text-sm font-medium space-x-1 text-gray-500">
                        <p>Didn't recieve code? </p> <a 
                        @click="sendOTPCodeToUserEmail()" 
                        class="flex flex-row items-center text-blue-600 cursor-pointer hover:underline" 
                        id='test-resent-otp-code-btn'
                        >
                        Resend
                        </a>
                    </div>
                    </div>
                </div>
     
            </div>
            </div>
        </div>
    </div>
</template>

<style scoped>

</style>