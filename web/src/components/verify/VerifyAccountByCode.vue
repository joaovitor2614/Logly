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




const otpDigit1: Ref<string> = ref('')
const otpDigit2: Ref<string> = ref('')
const otpDigit3: Ref<string> = ref('')
const otpDigit4: Ref<string> = ref('')
const otpDigit5: Ref<string> = ref('')
const otpDigit6: Ref<string> = ref('')

const resetOTCCodeDigits = () => {
    otpDigit1.value = ''
    otpDigit2.value = ''
    otpDigit3.value = ''
    otpDigit4.value = ''
    otpDigit5.value = ''
    otpDigit6.value = ''
}

const isDisabled = computed(() => otpDigit1.value && otpDigit2.value && otpDigit3.value && otpDigit4.value && otpDigit5.value && otpDigit6.value ? false : true);

const verifyOTPCode = async ()  => {
    const otpCode = otpDigit1.value + otpDigit2.value + otpDigit3.value + otpDigit4.value + otpDigit5.value + otpDigit6.value
    userStore.verifyPassedOTPCode(otpCode)
}


onMounted(() => {
    resetOTCCodeDigits()
    sendEmailVerificationCode()
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
                    <div class="flex flex-row items-center justify-between mx-auto w-full max-w-xs space-x-2">
                    <div class="w-16 h-16 ">
                        <input v-model="otpDigit1" class="w-full h-full flex flex-col items-center justify-center text-center px-5 outline-none rounded-xl border border-gray-200 text-lg bg-white focus:bg-gray-50 focus:ring-1 ring-blue-700" type="text" name="" id="">
                    </div>
                    <div class="w-16 h-16 ">
                        <input v-model="otpDigit2" class="w-full h-full flex flex-col items-center justify-center text-center px-5 outline-none rounded-xl border border-gray-200 text-lg bg-white focus:bg-gray-50 focus:ring-1 ring-blue-700" type="text" name="" id="">
                    </div>
                    <div class="w-16 h-16 ">
                        <input v-model="otpDigit3" class="w-full h-full flex flex-col items-center justify-center text-center px-5 outline-none rounded-xl border border-gray-200 text-lg bg-white focus:bg-gray-50 focus:ring-1 ring-blue-700" type="text" name="" id="">
                    </div>
                    <div class="w-16 h-16 ">
                        <input v-model="otpDigit4" class="w-full h-full flex flex-col items-center justify-center text-center px-5 outline-none rounded-xl border border-gray-200 text-lg bg-white focus:bg-gray-50 focus:ring-1 ring-blue-700" type="text" name="" id="">
                    </div>
                    <div class="w-16 h-16 ">
                        <input v-model="otpDigit5" class="w-full h-full flex flex-col items-center justify-center text-center px-5 outline-none rounded-xl border border-gray-200 text-lg bg-white focus:bg-gray-50 focus:ring-1 ring-blue-700" type="text" name="" id="">
                    </div>
                    <div class="w-16 h-16 ">
                        <input v-model="otpDigit6" class="w-full h-full flex flex-col items-center justify-center text-center px-5 outline-none rounded-xl border border-gray-200 text-lg bg-white focus:bg-gray-50 focus:ring-1 ring-blue-700" type="text" name="" id="">
                    </div>
                    </div>

                    <div class="flex flex-col space-y-5">
                    <div>
                    <div class="flex flex-col items-center justify-center">
                        <Button :buttonAction="verifyOTPCode" :is-disabled="isDisabled">
                        Verify Account
                        </Button>
                    </div>
             
                    </div>

                    <div class="flex flex-row items-center justify-center text-center text-sm font-medium space-x-1 text-gray-500">
                        <p>Didn't recieve code?</p> <a @click="sendEmailVerificationCode()" 
                        class="flex flex-row items-center text-blue-600 cursor-pointer hover:underline" 
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