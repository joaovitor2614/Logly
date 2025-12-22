<script setup lang="ts">
import Button from '@/components/common/Button.vue'
import DialogWrapper from '@/components/common/DialogWrapper.vue';
import { computed, reactive, Ref, ref } from 'vue';
import { WellIOType } from './types';
import WellSelector from '../../helpers/WellSelector.vue';
import useVuelidate from '@vuelidate/core';
import { required} from '@vuelidate/validators'
import { bottomGreaterThanOrEqualTop, topLessThanOrEqualBottom, createFormAttributeErrors } from '@/utils/validations';
import { useDialogStore, useWellStore } from '@/stores';


interface Props {
    WellIOType: `${WellIOType}`
}

const props = defineProps<Props>();
const isLoading: Ref<boolean> = ref(false);
const dialogStore = useDialogStore()
const wellStore = useWellStore();

interface Form {
    wellID: string,
    lasFile: undefined | File,
    top: Number | null,
    bottom: Number | null,
}
const form: Form = reactive({
    wellID: '',
    lasFile: undefined,
    bottom: null,
    top: null,
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


const importWell = () => {
    console.log('importWell')
}
</script>

<template>
    <DialogWrapper :cardTitle="`${props.WellIOType === 'import' ? 'Import' : 'Export'} Well`">
        <v-row class="d-flex justify-center mt-7">
            <v-col cols="10">
                <v-file-input
                    v-if="props.WellIOType == 'import'"
                    v-model="form.lasFile"
                    label="LAS File"
                ></v-file-input>
                <WellSelector v-else-if="props.WellIOType == 'export'" v-model:wellID="form.wellID" />

                
        
            </v-col>
            
        </v-row>
        <DepthIntervalSelector v-model:top="form.top" v-model:bottom="form.bottom" :topErrors="topErrors" :bottomErrors="bottomErrors"/>
        
    
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