<script setup lang="ts">
import { reactive, Ref, ref, watch } from 'vue';
import useVuelidate from '@vuelidate/core';
import { required} from '@vuelidate/validators'
import { computed } from 'vue';
import Button from '@/components/common/Button.vue'
import DialogWrapper from '@/components/common/DialogWrapper.vue';
import { useDialogStore, useWellStore } from '@/stores';
import DepthIntervalSelector from '@/components/welllog/DepthIntervalSelector.vue';
import { getWellBasicInfoFromFile } from '@/api/services/well';
import { TableWellLogsInfo } from '../welllogs/types';
import WellLogsTable from '../welllogs/WellLogsTable.vue';
import { bottomGreaterThanOrEqualTop, topLessThanOrEqualBottom, createFormAttributeErrors } from '@/utils/validations';


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
const topErrors = computed(() => createFormAttributeErrors(v$, 'top'))
const bottomErrors = computed(() => createFormAttributeErrors(v$, 'bottom'))
const importWell = async () => {
    isLoading.value = true

    const response = await wellStore.importNewFile(form.lasFile)
    console.log('response comp')
    isLoading.value = false
    if (response) {
        dialogStore.closeDialogWindow()
    }
}

const setWellBasicInfo = (wellBasicInfo: any) => {
    form.top = wellBasicInfo.min_value
    form.bottom = wellBasicInfo.max_value
    setWellLogTableItems(wellBasicInfo.well_logs)
}

const setWellLogTableItems = (wellLogsInfo: App.Well.WellLog[]) => {
    tableWellLogsInfo.value = []
    wellLogsInfo.forEach((wellLog) => {
        tableWellLogsInfo.value.push(
            { name: wellLog.mnemonic, unit: wellLog.unit, description: wellLog.description} 
        )
    })
    
}

watch(() => form.lasFile, async (value) => {
    if (value) {
        const response = await getWellBasicInfoFromFile(form.lasFile)
        if (response) {
            setWellBasicInfo(response.data)

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
                <DepthIntervalSelector v-model:top="form.top" v-model:bottom="form.bottom" :topErrors="topErrors" :bottomErrors="bottomErrors"/>
                <WellLogsTable
                    :wellLogsInfo="tableWellLogsInfo" 
                />

            
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