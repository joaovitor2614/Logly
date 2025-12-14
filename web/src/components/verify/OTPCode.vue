<script setup lang="ts">

import Button from '@/components/common/Button.vue'
interface Props {
    isDisabled: boolean,
    isLoadingVerify: boolean,
    sendOTPCode: () => void,
    verifyFunction: () => void,
}

const props = defineProps<Props>();
const otpCode = defineModel<string>('otpCode')


/**
 * Execute the verify function provided in the props
 * @returns {void}
 */

const executeVerifyFunction = () => {
    console.log('executeVerifyFunction')
    props.verifyFunction();
  
}

</script>

<template>

                
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
                                :buttonAction="executeVerifyFunction" 
                                :is-disabled="isVerifyDisabled"
                                :is-button-loading="props.isLoadingVerify"
                                :id="'test-verify-otp-btn'"
                                >
                                Verify 
                                </Button>
                            </div>
                
                        </div>
                    <div class="flex flex-row items-center justify-center text-center text-sm font-medium space-x-1 text-gray-500">
                        <p>Didn't recieve code? </p> <a 
                        @click="sendOTPCode()"
                        :is-disabled="isLoadingVerify || isLoadingVerify" 
                        class="flex flex-row items-center text-blue-600 cursor-pointer hover:underline" 
                        id='test-resent-otp-code-btn'
                        >
                        Resend
                        </a>
                    </div>
            </div>
    </div>
</template>

<style lang="scss" scoped>

</style>