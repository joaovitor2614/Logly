<script setup lang="ts">
import { usePlotStore } from '@/stores';
import { PlotType } from '../types';
import PlotView from './PlotView.vue';
import { computed } from 'vue';

interface Props {
    plotType: `${PlotType}`,
    title: string
}
const props = defineProps<Props>()

const plotStore = usePlotStore()
const template = computed(() => {
   return props.plotType === 'histogram' ? plotStore.histogramTemplate : plotStore.crossPlotTemplate;
})


</script>

<template>
     
      <v-col xs="12" md="12">
        <v-card outlined shaped elevation="2" class="pa-4 plot-card">
          <v-card-title class="font-weight-medium text-title-1">
            {{ props.title }}
          </v-card-title>
          <v-divider></v-divider>

          <v-card-text class="d-flex justify-start align-center">
          
            <div
            v-if="template"
            >
              <PlotView :plotType="props.plotType" :template="template"/>
            </div>
          </v-card-text>
        </v-card>
      </v-col>

</template>

<style scoped>
.plot-card {

  min-height: 60vh;
}
</style>