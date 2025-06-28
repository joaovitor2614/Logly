<script setup lang="ts">
import Button from '@/components/common/Button.vue'
import DialogWrapper from '@/components/common/DialogWrapper.vue';
import { useDialogStore, useWellStore } from '@/stores';
import { Ref, ref } from 'vue';



const wellStore = useWellStore()
const dialogStore = useDialogStore()


const selectedWell: Ref<string> = ref('');
const xAxisSelectedWellLog: Ref<string> = ref('');
const yAxisSelectedWellLog: Ref<string> = ref('');

const wellLogItems = ref([])
const wellItems = ref([])


const populateWellItems = () => {
    console.log('populateWellItems')
}

const createPlotView= () => {
    console.log('createPlotVIew')
}
</script>

<template>
    <DialogWrapper :cardTitle="'Plot Dialog'">
        <v-row>
            <v-col cols="10">
                <v-select
                    class="mt-4 mb-3"
                    :items="wellItems"
                    label="Well name"
                    v-model="selectedWell"
                    hide-details
                    outlined
                    dense
                ></v-select>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="6">
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