<script setup lang="ts">
import { PlotType } from '../types';
import PlotView from './PlotView.vue';
interface Props {
    plotType: `${PlotType}`,
    title: string
}
const props = defineProps<Props>()
</script>

<template>
     
      <v-col xs="12" md="12">
        <v-card outlined shaped elevation="2" class="pa-4">
          <v-card-title class="font-weight-medium text-title-1">
            {{ props.title }}
          </v-card-title>
          <v-divider></v-divider>

          <v-card-text class="d-flex justify-start align-center">
          
            <div
            >
              <PlotView :plotType="props.plotType" />
            </div>
          </v-card-text>
        </v-card>
      </v-col>

</template>

<style scoped>

</style>