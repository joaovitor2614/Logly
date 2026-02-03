<script setup lang="ts">
import { usePlotStore } from '@/stores';
import { PlotType } from '../types';
import PlotView from './PlotView.vue';
import { computed } from 'vue';
import PlotEdit from './PlotEdit.vue';

interface Props {
    plotType: `${PlotType}`,
    title: string
}
const props = defineProps<Props>()

const plotStore = usePlotStore()
const template = computed(() => {
  console.log('jasjojasjsjoiasjosal')
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

          <v-card-text>
            <v-container class="d-flex align-stretch pa-0" fluid>
                <div
            v-if="template"
            class="plot-wrapper"
            >
              <PlotView :plotType="props.plotType" :template="template"/>
             
            </div>
            <div class="plot-edit-wrapper" v-if="template"> 
              <PlotEdit />
            </div>
            </v-container>
          
          </v-card-text>
        </v-card>
      </v-col>

</template>

<style scoped>
.plot-card {
  min-height: 60vh;
}

/* left plot grows */
.plot-wrapper {
  flex: 1;
  min-width: 0; /* important for proper overflow handling */
  margin-right: 16px;
  display: flex;
}
.plot-wrapper .plot-canvas {
  width: 100%;
  height: 100%;
  min-height: 50vh;
}

/* right column: fixed width, scrollable */
.plot-edit-wrapper {
  width: 320px;
  max-width: 40%;
  padding-left: 12px;
  overflow: auto;
}
</style>