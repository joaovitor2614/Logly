<script setup lang="ts">
import Button from '@/components/common/Button.vue'
import DialogWrapper from '@/components/common/DialogWrapper.vue';
import WellSelector from '../../well/helpers/WellSelector.vue';
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
const form = reactive(getNewPlotTemplate(props.plotType))


const rules = {
    wellID: { required, $autoDirty: true },
    axes: {
        x: {
            id: { required, $autoDirty: true },
        },
        y: {
            id: { required, $autoDirty: true },
        },
    }

}

const v$ = useVuelidate(rules, form);

const isDisabled = computed(() => {
    const isDisabledHistogram = v$.value.axes.x.id.$invalid || v$.value.wellID.$invalid;
    const isDisabledCrossPlot = props.plotType == 'scatter' ? v$.value.axes.y.id.$invalid : false;

    return isDisabledHistogram || isDisabledCrossPlot
})

const selectedWellInfo = computed(() => wellStore.wells.find((well) => well._id === form.wellID))



const wellLogItems = computed(() => {

    if (selectedWellInfo.value) {
        return selectedWellInfo.value.welllogs.map((wellLog) => {
            return { title: wellLog.name, value: wellLog._id }
        })
    }
    return []
})

const setAxisWellLogRange = (axisKey: 'x' | 'y') => {
    const wellLogID = form.axes[axisKey].id;
    const wellLogsInfo = selectedWellInfo.value?.welllogs;
    const wellLogInfo = wellLogsInfo?.find((wellLog) => wellLog._id === wellLogID);
    if (!wellLogInfo) return
    form.axes[axisKey].range = [wellLogInfo.min_value, wellLogInfo.max_value]
    form.axes[axisKey].unit = wellLogInfo.unit
    form.axes[axisKey].name = wellLogInfo.name
}

const parsePlot = () => {
    setAxisWellLogRange('x')
    if (props.plotType === 'scatter') {
        setAxisWellLogRange('y')
    }
}


const createPlotView= () => {
    parsePlot()

    plotStore.registerPlot(form, props.plotType)
    dialogStore.closeDialogWindow()
   
}


</script>

<template>
    <DialogWrapper :cardTitle="'Plot Dialog'">
        <v-container class="d-flex flex-column justify-center pa-12">

            <WellSelector v-model:wellID="form.wellID" />
            
          
            <AxisWellLogSelection 
            
                :axis-name="'X'"
                :wellID="form.wellID" 
                :wellLogItems="wellLogItems" 
                v-model:wellLogAxis="form.axes.x" 
            />
            <AxisWellLogSelection 
                v-if="props.plotType === 'scatter'"
                :axis-name="'Y'"
                :wellID="form.wellID" 
                :wellLogItems="wellLogItems" 
                v-model:wellLogAxis="form.axes.y" 
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