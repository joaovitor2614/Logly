<script setup lang="ts">
import { Ref, ref } from 'vue';
import { useUserStore } from '@/stores';
interface Props {
    isDisabled: boolean,
    sendOTPCode: () => void
}

const props = defineProps<Props>();
const otpCode = defineModel('otpCode')
const isLoadingVerify: Ref<boolean> = ref(false);
const userStore = useUserStore();
const verifyOTPCode = async ()  => {
    isLoadingVerify.value = true
    userStore.verifyPassedOTPCode(otpCode.value)
    isLoadingVerify.value = false
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
                                :buttonAction="verifyOTPCode" 
                                :is-disabled="props.isDisabled"
                                :is-button-loading="isLoadingVerify"
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