<script setup lang="ts">
import { useAuthStore, useDialogStore, useUserStore } from '@/stores';
import DialogWrapper from '../common/DialogWrapper.vue';
import Button from '@/components/common/Button.vue'
import { useToast } from 'vue-toastification';
import { Ref, ref } from 'vue';

const dialogStore = useDialogStore()
const authStore = useAuthStore()
const userStore = useUserStore()
const toast = useToast()
const isLoading: Ref<boolean> = ref(false)
const deleteUserAccount = async () => {
    isLoading.value = true
    const response = await userStore.deleteUserAccount();
    if (response) {
        authStore.logout()
        toast.success('Account deleted successfully')
        dialogStore.closeDialogWindow()
    }
    isLoading.value = false
}
</script>

<template>
    <DialogWrapper cardTitle="Delete Account">
   
           
               <div class="mt-6 text-h6 text-medium-emphasis ps-4">
                  Are you sure you want to delete your account?
                </div> 
                 <v-divider class="mt-2"></v-divider>
                <v-container class="my-2 d-flex justify-end">
                    <Button 
                    :class="'mr-4'"
                    :buttonAction="dialogStore.closeDialogWindow"
                    >
                        Cancel
                    </Button>  
                    <Button 
  
                    :buttonAction="deleteUserAccount"
                 
                    :isButtonLoading="isLoading"
                    >
                        Delete
                    </Button>  
   
                </v-container>
      
  
    </DialogWrapper>
</template>

<style scoped>

</style>