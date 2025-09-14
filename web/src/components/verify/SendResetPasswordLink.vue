<script setup lang="ts">
import AuthBase from '../auth/AuthBase.vue';
import { sendResetPasswordLink } from '@/api/services/user';
import Button from '@/components/common/Button.vue'

import { Ref, ref, computed } from 'vue';

const emailAddress: Ref<string> = ref('')
const isLoading: Ref<boolean> = ref(false)
const executeResetPasswordLink = async () => {
    isLoading.value = true
    await sendResetPasswordLink(emailAddress.value)
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
                class="mb-5"
            />
            <Button 
                :buttonAction="executeResetPasswordLink" 
                :isDisabled="isDisabled"
                :isButtonLoading="isLoading"


                >
                Send Reset Password Link
            </Button>
        </form>

    </AuthBase>


</template>

<style lang="scss" scoped>

</style>