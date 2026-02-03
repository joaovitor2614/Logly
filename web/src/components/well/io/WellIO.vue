<script setup lang="ts">
import Button from '@/components/common/Button.vue'
import DialogWrapper from '@/components/common/DialogWrapper.vue';
import { computed, reactive, Ref, ref, watch } from 'vue';
import { WellIOType } from '../types';
import WellSelector from '../helpers/WellSelector.vue'
import useVuelidate from '@vuelidate/core';
import { required} from '@vuelidate/validators'
import { bottomGreaterThanOrEqualTop, topLessThanOrEqualBottom, createFormAttributeErrors } from '@/utils/validations';
import { useDialogStore, useWellStore } from '@/stores';
import { TableWellLogsInfo } from '../../welllogs/types';
import { getWellBasicInfoFromFile } from '@/api/services/well';
import WellLogsTable from  '@/components/well/welllogs/WellLogsTable.vue';
import DepthIntervalSelector from '@/components/welllog/DepthIntervalSelector.vue';



interface Props {
    wellIOType: `${WellIOType}`,

}

const props = defineProps<Props>();
const isLoading: Ref<boolean> = ref(false);
const dialogStore = useDialogStore()
const wellStore = useWellStore();



const tableWellLogsInfo: Ref<TableWellLogsInfo> = ref([])

interface Form {
    wellID: string,
    lasFile: undefined | File,
    top: Number | null,
    bottom: Number | null,
}

const form: Form = reactive({
    lasFile: undefined,
    bottom: null,
    top: null,
    wellID: '',
})

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
const bottomErrors = computed(() => createFormAttributeErrors(v$, 'bottom'));


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

const setWellBasicInfo = (wellBasicInfo: any) => {
    form.top = wellBasicInfo.min_value
    form.bottom = wellBasicInfo.max_value
    setWellLogTableItems(wellBasicInfo.well_logs)
}

const setWellLogTableItems = (wellLogsInfo: App.Well.WellLog[]) => {
    tableWellLogsInfo.value = []
    wellLogsInfo.forEach((wellLog) => {
        tableWellLogsInfo.value.push(
            { name: wellLog.name, unit: wellLog.unit, description: wellLog.description} 
        )
    })
    
}


watch(() => form.lasFile, async () => {
    if (form.lasFile) {
        const response = await getWellBasicInfoFromFile(form.lasFile)
        if (response) {
            setWellBasicInfo(response.data)

        }
        console.log('response.data', response.data)
    }   

})

watch(() => form.wellID, async (value) => {
    if (value) {
        const wellInfo = wellStore.wells.find(well => well._id == value)

        if (wellInfo) {
            setWellBasicInfo(wellInfo.welllogs)
        }
  
    }   

})



</script>

<template>
    <DialogWrapper :cardTitle="`${props.wellIOType === 'import' ? 'Import' : 'Export'} Well`">
        <v-row class="d-flex justify-center mt-7">
            <v-col cols="10">
                <v-file-input
                    v-if="props.wellIOType == 'import'"
                    v-model="form.lasFile"
                    label="LAS File"
                ></v-file-input>
                <WellSelector v-else-if="props.wellIOType == 'export'" v-model:wellID="form.wellID" />

                
        
            </v-col>
            
        </v-row>
        <DepthIntervalSelector 
            v-model:top="form.top" 
            v-model:bottom="form.bottom" 
            :topErrors="topErrors" 
            :bottomErrors="bottomErrors"
        />
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
    </DialogWrapper>
</template>

<style scoped>

</style>