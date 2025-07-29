<script setup lang="ts">
import { reactive } from 'vue';
import useVuelidate from '@vuelidate/core';
import { required} from '@vuelidate/validators'
import { computed } from 'vue';
import Button from '@/components/common/Button.vue'


import DialogWrapper from '../../common/DialogWrapper.vue';
import { useDialogStore, useWellStore } from '@/stores';

const dialogStore = useDialogStore()
const wellStore = useWellStore();
const form = reactive({
    lasFile: '',
    wellName: ''
})

const rules = {
    lasFile: { required, $autoDirty: true },
    wellName: { required, $autoDirty: true }
}
const v$ = useVuelidate(rules, form);
const isDisabled = computed(() => v$.value.lasFile.$invalid || v$.value.wellName.$invalid ? true : false);
const importWell = async () => {
    const response = await wellStore.importNewFile(form.lasFile, form.wellName)
    if (response) {
        dialogStore.closeDialogWindow()
    }
}


</script>

<template>
    <DialogWrapper cardTitle="Import Well">
                  <v-row>
                    <v-col cols="6">
                        <v-file-input
                            accept="image/*"
                            v-model="form.lasFile"
                            label="LAS File"
                        ></v-file-input>
               
                    </v-col>
                     <v-col cols="6">
                        <v-text-field 
                        type="text" 
                        v-model="form.wellName"
                        label="Well name" 
            
            
                        />
                    </v-col>
                </v-row>

            
                <v-card-actions>
        
                    <Button 
                    :id="'test-import-cancel-btn'"
                    :buttonAction="dialogStore.closeDialogWindow"
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