<script setup lang="ts">
import Button from '@/components/common/Button.vue'
import DialogWrapper from '@/components/common/DialogWrapper.vue';
import { useDialogStore, useWellStore, usePlotStore } from '@/stores';
import { computed, reactive } from 'vue';
import useVuelidate from '@vuelidate/core';
import { required } from '@vuelidate/validators'
import { PlotType } from '../types';
import AxisWellLogSelection from './AxisWellLogSelection.vue';
import { getNewPlotTemplate } from '@/utils/getNewPloTemplate'

interface Props {
    plotType: `${PlotType}`,
}

const props = defineProps<Props>();

const wellStore = useWellStore()
const dialogStore = useDialogStore()
const plotStore = usePlotStore()
const form = reactive(getNewPlotTemplate())


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
    dialogStore.closeDialogWindow()
   
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
            <AxisWellLogSelection 
            
                :axis-name="'X'" 
                :wellLogItems="wellLogItems" 
                v-model:wellLogID="form.xWellLogID" 
            />
            <AxisWellLogSelection 
                v-if="props.plotType === 'scatter'"
                :axis-name="'Y'" 
                :wellLogItems="wellLogItems" 
                v-model:wellLogID="form.yWellLogID" 
            />


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