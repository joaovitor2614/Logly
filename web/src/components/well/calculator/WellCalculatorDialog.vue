<script setup lang="ts">
import WellSelector from '@/components/well/helpers/WellSelector.vue';
import DialogWrapper from '@/components/common/DialogWrapper.vue';
import Button from '@/components/common/Button.vue'
import useVuelidate from '@vuelidate/core';
import { required} from '@vuelidate/validators'
import {  reactive, computed } from 'vue';
import { useDialogStore, useWellStore } from '@/stores';
import { calculateWellLog } from '@/api/services/well';
import { useToast } from 'vue-toastification';

const form = reactive({
    wellID: '',
    formula: '',
    outputWellLogName: '',
    outputWellLogUnit: ''
})

const toast = useToast()
const dialogStore = useDialogStore()
const wellStore = useWellStore();
const executeCalculation = async () => {
    const response = await calculateWellLog(
        form.wellID,
        form.formula,
        form.outputWellLogName,
        form.outputWellLogUnit
    );
    if (response) {
        toast.success('Well log calculated successfully');
        dialogStore.closeDialogWindow();
        wellStore.getWells();
    }
  
}



const rules = {
    wellID: { required, $autoDirty: true },
    formula: { required, $autoDirty: true },
    outputWellLogName: { required, $autoDirty: true },
    outputWellLogUnit: { required, $autoDirty: true },
}
const v$ = useVuelidate(rules, form);

const isDisabled = computed(() => {
    return v$.value.wellID.$invalid || 
    v$.value.formula.$invalid || 
    v$.value.outputWellLogName.$invalid || 
    v$.value.outputWellLogUnit.$invalid
});
</script>

<template>
    <DialogWrapper :cardTitle="'Well Calculator'">
        <v-container class="d-flex flex-column justify-center pa-12">
            <WellSelector v-model:wellID="form.wellID" />
            <v-text-field
                v-model="form.formula"
                label="Well log calculator as a python expression (e.g., GR + 10)"
                outlined
                class="mt-4"
            ></v-text-field>
            <p class="mb-5 mt-5 text-center">Output</p>
            <v-divider></v-divider>
            <v-container class="d-flex justify-center align-center">
                <v-text-field
                    v-model="form.outputWellLogName"
                    label="Output well log name"
                    outlined
                    class="mt-4"
                ></v-text-field>
                <v-text-field
                    v-model="form.outputWellLogUnit"
                    label="Output well log unit"
                    outlined
                    class="mt-4"
                ></v-text-field>
            </v-container>
         
        </v-container>
        <v-card-actions>
            <Button 
            :buttonAction="dialogStore.closeDialogWindow"
            >
                Cancel
            </Button>  
            <Button 
                :button-action="executeCalculation"
                :is-disabled="isDisabled"
                >Calculate
            </Button> 
        </v-card-actions>     


   
          
     
    </DialogWrapper>
</template>

<style lang="scss" scoped>

</style>