<script setup lang="ts">
import { useDialogStore } from '@/stores';
import DialogWrapper from '../common/DialogWrapper.vue';
import Button from '@/components/common/Button.vue'

const dialogStore = useDialogStore()
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
  
                    :buttonAction="dialogStore.closeDialogWindow"
                    >
                        Delete
                    </Button>  
   
                </v-container>
      
  
    </DialogWrapper>
</template>

<style scoped>

</style>