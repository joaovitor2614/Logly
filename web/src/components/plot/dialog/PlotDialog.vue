<script setup lang="ts">
import Button from '@/components/common/Button.vue'
import DialogWrapper from '@/components/common/DialogWrapper.vue';
import { useDialogStore, useWellStore, usePlotStore } from '@/stores';
import { computed, reactive } from 'vue';
import useVuelidate from '@vuelidate/core';
import { required } from '@vuelidate/validators'
import { PlotType } from '../types';

interface Props {
    plotType: `${PlotType}`,
}

const props = defineProps<Props>();

const wellStore = useWellStore()
const dialogStore = useDialogStore()
const plotStore = usePlotStore()
const form = reactive({
    wellID: '',
    xWellLogID: '',
    yWellLogID: '',
})


const rules = {
    wellID: { required, $autoDirty: true },
    xWellLogID: { required,  $autoDirty: true },
    yWellLogID: { required,  $autoDirty: true },
}

const v$ = useVuelidate(rules, form);

const isDisabled = computed(() => {
    const isDisabledHistogram = v$.value.xWellLogID.$invalid || v$.value.wellID.$invalid;
    const isDisabledCrossPlot = props.plotType == 'scatter' ? v$.value.yWellLogID.$invalid : false;

    return isDisabledHistogram || isDisabledCrossPlot
})


const wellItems = computed(() => wellStore.wells.map((well) => {
    return { title: well.name, value: well._id }}))

const wellLogItems = computed(() => {
    const well = wellStore.wells.find((well) => well._id === form.wellID)
    if (well) {
        return well.welllogs.map((wellLog) => {
            return { title: wellLog.name, value: wellLog._id }
        })
    }
})


const createPlotView= () => {
    plotStore.registerPlot(form, props.plotType)
   
}


</script>

<template>
    <DialogWrapper :cardTitle="'Plot Dialog'">
        <v-container class="d-flex flex-column justify-center pa-12">

   
            <v-select
                        
            class="mt-4 mb-3"
            :items="wellItems"
            label="Well name"
            id="test-selected-wells-to-plot-selector"
            v-model="form.wellID"
            hide-details
            outlined
            dense
            />
            <p class="mb-5 mt-5 text-center">X-Axis</p>
            <v-divider></v-divider>
            <v-select
                class="mt-4"
                :items="wellLogItems"
                label="Well log name"
                v-model="form.xWellLogID"
                hide-details
                outlined
                dense
            ></v-select>
            <p v-if="props.plotType === 'scatter'" class="mb-5 mt-5 text-center">Y-Axis</p>
            <v-divider></v-divider>
            <v-select
                v-if="props.plotType === 'scatter'"
            
                class="mt-4"
                :items="wellLogItems"
                label="Well log name"
                v-model="form.yWellLogID"
                hide-details
                outlined
                dense
            ></v-select>
        </v-container>

        <v-card-actions>
            <Button 
            :id="'test-plot-cancel-btn'"
            :buttonAction="dialogStore.closeDialogWindow"
            >
                Cancel
            </Button>  
            <Button 
            :button-action="createPlotView"
            :id="'test-plot-dialog-btn'"
            :isDisabled="isDisabled"
            
            >Import</Button> 
        </v-card-actions>     

  
    </DialogWrapper>
</template>

<style scoped>

</style>