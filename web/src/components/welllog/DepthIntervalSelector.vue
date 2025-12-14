<script setup lang="ts">
interface Props {
  topErrors: string[],
  bottomErrors: string[]
}
const props = defineProps<Props>();
import {  ModelRef } from 'vue'

const top: ModelRef<null | number> = defineModel('top', { required: true })
const bottom: ModelRef<null | number> = defineModel('bottom', { required: true })
</script>

<template>
    <v-row class="d-flex align-center justify-center mt-8 mb-8">
        <div class="text-h5">Depth Interval Selection</div>
    </v-row>
  <v-row class="d-flex align-center justify-center mt-8 mb-8">
    <v-col cols="4" class="pa-0">
      <v-text-field
        v-model="top"
        label="Top"
        :error-messages="props.topErrors"
        class="mr-2"
        outlined
        dense
      />
    </v-col>
    <v-col cols="4" class="pa-0">
      <v-text-field
        v-model="bottom"
        label="Bottom"
        :error-messages="props.bottomErrors"
        class="mr-2"
        outlined
        dense
      />
    </v-col>
  </v-row>
</template>

<style lang="scss" scoped></style>