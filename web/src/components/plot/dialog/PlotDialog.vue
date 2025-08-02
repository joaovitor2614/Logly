<script setup lang="ts">
import Button from '@/components/common/Button.vue'
import DialogWrapper from '@/components/common/DialogWrapper.vue';
import { useDialogStore, useWellStore } from '@/stores';
import { Ref, ref, onMounted, computed } from 'vue';



const wellStore = useWellStore()
const dialogStore = useDialogStore()


const selectedWellID: Ref<string> = ref('');
const xAxisSelectedWellLog: Ref<string> = ref('');
const yAxisSelectedWellLog: Ref<string> = ref('');


const wellItems = computed(() => wellStore.wells.map((well) => {
    return { text: well.name, value: well._id }}))

const wellLogItems = computed(() => {
    const well = wellStore.wells.find((well) => well._id === selectedWellID.value)
    if (well) {
        return well.welllogs.map((wellLog) => {
            return { text: wellLog.mnemonic, value: wellLog._id }
        })
    }
})
const populateWellItems = () => {
    console.log('populateWellItems')
}

const createPlotView= () => {
    console.log('createPlotVIew')
}

onMounted(() => {
    console.log('wellStore', wellStore.wells)
})
</script>

<template>
    <DialogWrapper :cardTitle="'Plot Dialog'">
        <div  class="d-flex flex-column  justify-center">
            <v-row>
                <v-col cols="10">
                    <v-select
                        
                        class="mt-4 mb-3"
                        :items="wellItems"
                        label="Well name"
                        id="test-selected-wells-to-plot-selector"
                        v-model="selectedWellID"
                        hide-details
                        outlined
                        dense
                    ></v-select>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="10">
                    <p class="font-weight-bold text-center mt-3 mb-6">
                        X-Axis
                    </p> 
                    <v-divider />
                </v-col>
            </v-row>
            <v-row >
                <v-col cols="10">
                    <v-select
                        class="mx-10 mb-1"
                        :items="wellLogItems"
                        label="Well log name"
                        v-model="xAxisSelectedWellLog"
                        hide-details
                        outlined
                        dense
                    ></v-select>
                </v-col>
            </v-row>
        </div>
        
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
            
            >Import</Button> 
        </v-card-actions>     

  
    </DialogWrapper>
</template>

<style scoped>

</style>