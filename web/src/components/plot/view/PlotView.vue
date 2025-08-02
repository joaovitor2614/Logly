<script setup lang="ts">
import { usePlotStore } from '@/stores';
//import Plotly from "plotly.js-dist/plotly";
const plotStore = usePlotStore()
var x1 = [];
for (var i = 1; i < 500; i++) {
  
	x1.push(Math.random() + 1);
}
var trace1 = {
  x: x1,
  type: "histogram",
  opacity: 0.5,
  marker: {
     color: 'green',
  },
};
var data = [trace1];
//Plotly.newPlot('plotDiv', data);

</script>

<template>
    <div id="plotDiv">

    </div>
</template>

<style scoped>

</style>