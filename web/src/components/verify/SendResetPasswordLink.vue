<script setup>
import Button from '@/components/common/Button.vue'
const sendResetPasswordLink = async () => {
    console.log('sendResetPasswordLink')

}
</script>

<template>

    <div class="relative flex min-h-screen flex-col justify-center overflow-hidden bg-gray-50 py-12">
        <div class="relative bg-white px-6 pt-10 pb-9 shadow-xl mx-auto w-full max-w-lg rounded-2xl">
            <div class="flex flex-col">
            <div class="flex flex-col text-center mb-8">
                <div class="font-semibold text-3xl">
                    <p>Password Reset</p>
                </div>
         
            </div>

            <div>
         
                <div class="flex flex-col space-y-16">
                    <v-text-field
                        name="email"
                        label="Email Address"
                        type="email"
                        placeholder="email"
                        class="mb-5"
                    />
                    <div class="flex flex-col space-y-5">
                    <div>
                    <div class="flex flex-col items-center justify-center mb-4">
                        <Button 
                        :buttonAction="sendResetPasswordLink" 
          
           
                        >
                        Send Reset Password Link
                        </Button>
                    </div>
             
                    </div>

            
                    </div>
                </div>
     
            </div>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>

</style>