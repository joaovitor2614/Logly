<script setup lang="ts">

import { PlotType } from '../types';

interface Props {
    plotType: `${PlotType}`,
}

const props = defineProps<Props>();



</script>

<template>
    <div id="plotDiv">
    
    </div>
</template>

<style scoped>

</style>