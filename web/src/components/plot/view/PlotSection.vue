<template>
  <v-container fluid>


    <v-row dense>

      <v-col xs="12" md="6">
        <v-card outlined shaped elevation="2" class="pa-4">
          <v-card-title class="font-weight-medium text-subtitle-1">
            Crossplot
          </v-card-title>
          <v-divider></v-divider>

          <v-card-text class="d-flex justify-center align-center" style="height: 350px;">
      
            <div
              style="
                width: 100%;
                height: 100%;
                border: 2px dashed #ccc;
                border-radius: 8px;
                display: flex;
                align-items: center;
                justify-content: center;
                color: #999;
                font-style: italic;
                font-size: 1.1rem;
              "
            >
              <PlotView :plotType="'crossplot'" />
            </div>
          </v-card-text>
        </v-card>
      </v-col>

 
      <v-col xs="12" md="6">
        <v-card outlined shaped elevation="2" class="pa-4">
          <v-card-title class="font-weight-medium text-subtitle-1">
            Histogram
          </v-card-title>
          <v-divider></v-divider>

          <v-card-text class="d-flex justify-center align-center" style="height: 350px;">
          
            <div
              style="
                width: 100%;
                height: 100%;
                border: 2px dashed #ccc;
                border-radius: 8px;
                display: flex;
                align-items: center;
                justify-content: center;
                color: #999;
                font-style: italic;
                font-size: 1.1rem;
              "
            >
              <PlotView :plotType="'histogram'" />
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import PlotView from './PlotView.vue';


</script>

<style scoped>

</style>