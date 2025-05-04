<script setup lang="ts">
import { ref } from 'vue'
interface Props {
    form: Record<string, string>,
    errorsMessages: Record<string, string[]>,
    authType: 'register' | 'login'
}

const props = defineProps<Props>();

const showPassword = ref(false);
const showConfirmPassword = ref(false);
</script>

<template>
         <v-text-field
                    v-if="props.authType === 'register'"
                    id='test-name-input'
                    v-model="props.form.name"
                    :error-messages="props.errorsMessages.name"
                    name="name"
                    label="User Name"
                    type="text"
                    placeholder="name"
         
                    required
                ></v-text-field>
                <v-text-field
                    v-if="props.authType === 'login' || props.authType === 'register'"
                    v-model="props.form.email"
                    :error-messages="props.errorsMessages.email"
                    name="email"
                    label="Email Address"
                    type="email"
                    id='test-email-input'

                    placeholder="email"
         
                    required
                ></v-text-field>
                <v-text-field
                    v-if="props.authType === 'login' || props.authType === 'register'"
                    v-model="props.form.password"
                    :error-messages="props.errorsMessages.password"
                    :type="showPassword ? 'text' : 'password'"
                    :append-inner-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                    @click:append-inner="showPassword = !showPassword"
                    name="password"
                    id='test-password-input'
                    label="Password"
        
                    placeholder="password"
                    required
                ></v-text-field>
                <v-text-field 
                    v-if="props.authType === 'register'"
                    v-model="props.form.confirmPassword"
                    :error-messages="props.errorsMessages.confirmPassword"
                    :type="showConfirmPassword ? 'text' : 'password'"
                    :append-inner-icon="showConfirmPassword ? 'mdi-eye' : 'mdi-eye-off'"
                    @click:append-inner="showConfirmPassword = !showConfirmPassword"
                    name="confirmPassword"
                    label="Confirm Password"
                    id='test-confirm-password-input'
                    placeholder="cocnfirm password"
          
                    required
                ></v-text-field>
                
</template>

<style scoped>

</style>