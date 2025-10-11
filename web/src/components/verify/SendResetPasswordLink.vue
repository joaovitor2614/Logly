<script setup lang="ts">
import AuthBase from '../auth/AuthBase.vue';
import { sendResetPasswordLink } from '@/api/services/user';
import Button from '@/components/common/Button.vue'

import { Ref, ref, computed } from 'vue';
import { useToast } from 'vue-toastification';

const emailAddress: Ref<string> = ref('')
const isLoading: Ref<boolean> = ref(false);
const toast = useToast()
const executeResetPasswordLink = async () => {
    isLoading.value = true
    const response = await  sendResetPasswordLink(emailAddress.value)
    if (response) {
        toast.success('Password reset link sent successfully!')
    }
    isLoading.value = false
}
const isDisabled = computed(() => emailAddress.value ? false : true);
</script>

<template>
    <AuthBase :helperTitle="'Send password reset link'">
        <form>
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
                :buttonAction="executeResetPasswordLink" 
                :isDisabled="isDisabled"
                :isButtonLoading="isLoading"


                >
                Send
            </Button>
             </div>
    
        </form>

    </AuthBase>


</template>

<style lang="scss" scoped>

</style>