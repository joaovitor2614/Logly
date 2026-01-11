vue3<script setup>
import WellSelector from '@/components/well/helpers/WellSelector.vue';
import DialogWrapper from '@/components/common/DialogWrapper.vue';
import Button from '@/components/common/Button.vue'
import {  reactive } from 'vue';
import { useDialogStore } from '@/stores';

const form = reactive({
    wellID: ''
})

const dialogStore = useDialogStore()
const executeCalculation = () => {
    console.log('executeCalculation')
}
</script>

<template>
    <DialogWrapper :cardTitle="'Well Calculator'">
        <v-container class="d-flex flex-column justify-center pa-12">
            <WellSelector v-model:wellID="form.wellID" />
        </v-container>
        <v-card-actions>
            <Button 
            :buttonAction="dialogStore.closeDialogWindow"
            >
                Cancel
            </Button>  
            <Button 
                :button-action="executeCalculation"
                
                >Calculate
            </Button> 
        </v-card-actions>     


   
          
     
    </DialogWrapper>
</template>

<style lang="scss" scoped>

</style>