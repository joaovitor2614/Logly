<script setup lang="ts">
import { Ref, ref } from 'vue';
import { useUserStore } from '@/stores';
import Button from '@/components/common/Button.vue'
interface Props {
    isDisabled: boolean,
    isLoadingVerify: boolean,
    sendOTPCode: () => void,
    verifyFunction: () => void,
}

const props = defineProps<Props>();
const otpCode = defineModel('otpCode')
const isLoadingVerify: Ref<boolean> = ref(false);
const userStore = useUserStore();

/*************  ✨ Windsurf Command ⭐  *************/
/**
 * Execute the verify function provided in the props
 * @returns {void}
 */

/*******  c8e84a27-2d1e-409b-8ec7-e88e17da258d  *******/
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