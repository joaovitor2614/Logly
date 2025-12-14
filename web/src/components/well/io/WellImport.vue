<script setup lang="ts">
import { reactive, Ref, ref } from 'vue';
import useVuelidate from '@vuelidate/core';
import { required} from '@vuelidate/validators'
import { computed } from 'vue';
import Button from '@/components/common/Button.vue'
import DialogWrapper from '../../common/DialogWrapper.vue';
import { useDialogStore, useWellStore } from '@/stores';


const isLoading: Ref<boolean> = ref(false)
const dialogStore = useDialogStore()
const wellStore = useWellStore();

interface Form {
    lasFile: undefined | File
}
const form: Form = reactive({
    lasFile: undefined,
})

const rules = {
    lasFile: { required, $autoDirty: true },
}
const v$ = useVuelidate(rules, form);
const isDisabled = computed(() => v$.value.lasFile.$invalid ? true : false);
const importWell = async () => {
    isLoading.value = true

    const response = await wellStore.importNewFile(form.lasFile)
    isLoading.value = false
    if (response) {
        dialogStore.closeDialogWindow()
    }
}


</script>

<template>
    <DialogWrapper cardTitle="Import Well">
                <v-row>
                    <v-col cols="10">
                        <v-file-input
               
                            v-model="form.lasFile"
                            label="LAS File"
                        ></v-file-input>
               
                    </v-col>
                </v-row>

            
                <v-card-actions>
        
                    <Button 
                    :id="'test-import-cancel-btn'"
                    :buttonAction="dialogStore.closeDialogWindow"
                    :is-button-loading="isLoading"
                    >
                        Cancel
                    </Button>  
                    <Button 
                    :id="'test-import-well-btn'"
                    :buttonAction="importWell"
                    :is-disabled="isDisabled"
                    
                    >Import</Button> 
                </v-card-actions>     
        
        </DialogWrapper >
</template>

<style scoped>

</style>