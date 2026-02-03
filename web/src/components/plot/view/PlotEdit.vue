<script setup lang="ts">
interface Props {
  template: App.Plot.Template
}

const props = defineProps<Props>();
</script>

<template>
  <v-container class="pa-2 plot-edit">
    <p class="text-h6 font-weight-medium mb-4">Axis</p>
    <v-divider></v-divider>
    <p class="font-weight-small mb-4">X</p>
    <v-row>
      <v-col cols="12" sm="6">
        <v-text-field v-model="props.template.axes.x.range[0]"></v-text-field>
      </v-col>
      <v-col cols="12" sm="6">
        <v-text-field v-model="props.template.axes.x.range[1]"></v-text-field>
      </v-col>
    </v-row>
    <p class="font-weight-small mb-4" v-if="template.type == 'scatter'">Y</p>
    <v-row v-if="template.type == 'scatter'">
        <v-col cols="12" sm="6">
          <v-text-field v-model="props.template.axes.y.range[0]"></v-text-field>
        </v-col>
        <v-col cols="12" sm="6">
          <v-text-field v-model="props.template.axes.y.range[1]"></v-text-field>
        </v-col>
    </v-row>
    <p class="text-h6 font-weight-medium mb-4">Color</p>
     <v-row>
      <v-col cols="12" sm="6">
      <v-color-picker
        v-model="template.color"
        elevation="0"
      ></v-color-picker>
      </v-col>
     
    </v-row>
  </v-container>
</template>

<style scoped>
.plot-edit {
  display: block;
}
</style>