<script setup lang="ts">
import Button from '@/components/common/Button.vue'
import DialogWrapper from '@/components/common/DialogWrapper.vue';
import { useDialogStore, useWellStore, usePlotStore } from '@/stores';
import { Ref, ref, computed, reactive } from 'vue';
import useVuelidate from '@vuelidate/core';
import { required, email, sameAs } from '@vuelidate/validators'
import { PlotType } from '../types';

interface Props {
    plotType: `${PlotType}`,
}

const props = defineProps<Props>();

const wellStore = useWellStore()
const dialogStore = useDialogStore()
const plotStore = usePlotStore()
const form = reactive({
    selectedWellID: '',
    xAxisSelectedWellLog: '',
    yAxisSelectedWellLog: '',
})


const rules = {
    selectedWellID: { required, $autoDirty: true },
    xAxisSelectedWellLog: { required,  $autoDirty: true },
    yAxisSelectedWellLog: { required,  $autoDirty: true },
}

const v$ = useVuelidate(rules, form);

const isDisabled = computed(() => {
    const isDisabledHistogram = v$.value.xAxisSelectedWellLog.$invalid || v$.value.selectedWellID.$invalid;
    const isDisabledCrossPlot = props.plotType == 'scatter' ? v$.value.yAxisSelectedWellLog.$invalid : false;

    return isDisabledHistogram || isDisabledCrossPlot
})


const wellItems = computed(() => wellStore.wells.map((well) => {
    return { title: well.name, value: well._id }}))

const wellLogItems = computed(() => {
    const well = wellStore.wells.find((well) => well._id === form.selectedWellID)
    if (well) {
        return well.welllogs.map((wellLog) => {
            return { title: wellLog.name, value: wellLog._id }
        })
    }
})


const createPlotView= () => {
    plotStore.registerPlot(
        form.xAxisSelectedWellLog,
        form.yAxisSelectedWellLog,
        form.selectedWellID
    )
   
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
            v-model="form.selectedWellID"
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
                v-model="form.xAxisSelectedWellLog"
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
                v-model="form.yAxisSelectedWellLog"
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