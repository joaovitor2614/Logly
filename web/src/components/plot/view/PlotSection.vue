<template>
  <v-container fluid>




      <v-col xs="12" md="12">
        <v-card outlined shaped elevation="2" class="pa-4">
          <v-card-title class="font-weight-medium text-title-1">
            Crossplot
          </v-card-title>
          <v-divider></v-divider>

          <v-card-text class="d-flex justify-start align-center" style="height: 350px;">
      
            <div
            >
              <PlotView :plotType="'crossplot'" />
            </div>
          </v-card-text>
        </v-card>
      </v-col>

 
      <v-col xs="12" md="12">
        <v-card outlined shaped elevation="2" class="pa-4">
          <v-card-title class="font-weight-medium text-title-1">
            Histogram
          </v-card-title>
          <v-divider></v-divider>

          <v-card-text class="d-flex justify-start align-center">
          
            <div
            >
              <PlotView :plotType="'histogram'" />
            </div>
          </v-card-text>
        </v-card>
      </v-col>

  </v-container>
</template>

<script setup>
import PlotView from './PlotView.vue';


</script>

<style scoped>

</style>