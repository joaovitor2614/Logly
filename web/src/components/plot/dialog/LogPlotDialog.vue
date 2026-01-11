<script setup>
import WellSelector from '@/components/well/helpers/WellSelector.vue';
import DialogWrapper from '@/components/common/DialogWrapper.vue';
import { getNewPlotTemplate } from '@/utils/getNewPloTemplate'
import {  reactive } from 'vue';

const form = reactive(getNewPlotTemplate('logplot'))
</script>

<template>
    <DialogWrapper :cardTitle="'Plot LogPlot'">
        <v-container class="d-flex flex-column justify-center pa-12">
            <WellSelector v-model:wellID="form.wellID" />
            <v-row class="mt-7">
                <v-cols cols="6" class="mr-3">
                    <v-btn dark icon small color="transparent">
                        <v-icon dark>mdi-layers-plus</v-icon>
                    </v-btn>
                    <span >Add Track</span>
                </v-cols>
                <v-cols cols="6" class="ml-3">
                    <v-btn dark icon small color="transparent" background-color="transparent">
                        <v-icon dark>mdi-layers-minus</v-icon>
                    </v-btn>
                    <span >Remove Track</span>
                </v-cols>
            </v-row>
    
        </v-container>
        
          
     
    </DialogWrapper>
</template>

<style lang="scss" scoped>

</style>