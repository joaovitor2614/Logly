<script setup lang="ts">
import { reactive, Ref, ref, watch } from 'vue';
import useVuelidate from '@vuelidate/core';
import { required} from '@vuelidate/validators'
import { computed } from 'vue';
import Button from '@/components/common/Button.vue'
import DialogWrapper from '../../common/DialogWrapper.vue';
import { useDialogStore, useWellStore } from '@/stores';
import DepthIntervalSelector from '@/components/welllog/DepthIntervalSelector.vue';
import { getWellBasicInfoFromFile } from '@/api/services/well';
import { TableWellLogsInfo } from '../welllogs/types';


const isLoading: Ref<boolean> = ref(false)
const dialogStore = useDialogStore()
const wellStore = useWellStore();

interface Form {
    lasFile: undefined | File,
    top: Number,
    bottom: Number
}
const form: Form = reactive({
    lasFile: undefined,
    bottom: 2000,
    top: 1000,
})
//const wellLogsInfo: Ref<TableWellLogsInfo[]> = ref([])
const rules = {
    lasFile: { required, $autoDirty: true },
}
const v$ = useVuelidate(rules, form);
const isDisabled = computed(() => {
    return v$.value.lasFile.$invalid || isLoading.value
});
const importWell = async () => {
    isLoading.value = true

    const response = await wellStore.importNewFile(form.lasFile)
    console.log('response comp')
    isLoading.value = false
    if (response) {
        dialogStore.closeDialogWindow()
    }
}

const setWellBasicInfo = (data: any) => {
    form.top = response.data.min
    form.bottom = response.data.max
}

watch(() => form.lasFile, async (value) => {
    if (value) {
        const response = await getWellBasicInfoFromFile(form.lasFile)
        if (response) {
            setWellBasicInfo(response.data)
            form.top = response.data.min
            form.bottom = response.data.max
        }
        console.log('response.data', response.data)
    }   
    

})

</script>

<template>
    <DialogWrapper cardTitle="Import Well">
                <v-row class="d-flex justify-center mt-7">
                    <v-col cols="10">
                        <v-file-input
               
                            v-model="form.lasFile"
                            label="LAS File"
                        ></v-file-input>
               
                    </v-col>
                </v-row>
                <DepthIntervalSelector v-model:top="form.top" v-model:bottom="form.bottom"/>

            
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