<template>
  <v-container fluid>
      <PlotCard :plotType="'scatter'" :title="'Crossplot'" />
      <PlotCard :plotType="'histogram'" :title="'Histogram'" />

  </v-container>
</template>

<script setup>
import PlotCard from './PlotCard.vue';
import PlotView from './PlotView.vue';


</script>

<style scoped>

</style>