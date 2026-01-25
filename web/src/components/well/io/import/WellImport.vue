<script setup lang="ts">
import { reactive, Ref, ref, watch } from 'vue';
import useVuelidate from '@vuelidate/core';
import { required} from '@vuelidate/validators'
import { computed } from 'vue';
import Button from '@/components/common/Button.vue'
import DialogWrapper from '@/components/common/DialogWrapper.vue';
import { useDialogStore, useWellStore } from '@/stores';
import { TableWellLogsInfo } from '@/components/well/welllogs/types';
import { bottomGreaterThanOrEqualTop, topLessThanOrEqualBottom, } from '@/utils/validations';
import WellIO from './WellIO.vue';


const isLoading: Ref<boolean> = ref(false);
const tableWellLogsInfo: Ref<TableWellLogsInfo> = ref([])
const dialogStore = useDialogStore()
const wellStore = useWellStore();

interface Form {
    lasFile: undefined | File,
    top: Number | null,
    bottom: Number | null,
}
const form: Form = reactive({
    lasFile: undefined,
    bottom: null,
    top: null,
})
//const wellLogsInfo: Ref<TableWellLogsInfo[]> = ref([])
const rules = {
    lasFile: { required, $autoDirty: true },
    top: { required, topLessThanOrEqualBottom, $autoDirty: true },
    bottom: { required, bottomGreaterThanOrEqualTop, $autoDirty: true }
}




const v$ = useVuelidate(rules, form);
const isDisabled = computed(() => {
    return v$.value.lasFile.$invalid || v$.value.top.$invalid || v$.value.bottom.$invalid ||isLoading.value
});

const importWell = async () => {
    isLoading.value = true
    if (!form.lasFile) {
        return
    }
    const response = await wellStore.importNewFile(form.lasFile)
    console.log('response comp')
    isLoading.value = false
    if (response) {
        dialogStore.closeDialogWindow()
    }
}





</script>

<template>
    <DialogWrapper cardTitle="Import Well">
                <WellIO :wellIOType="'import'"/>



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