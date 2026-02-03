<script setup lang="ts">

</script>

<template>
  <v-container class="pa-2 plot-edit">
    <p class="text-h6 font-weight-medium mb-4">Axis</p>
    <v-row>
      <v-col cols="12" sm="6">
        <v-text-field></v-text-field>
      </v-col>
      <v-col cols="12" sm="6">
        <v-text-field></v-text-field>
      </v-col>
    </v-row>
    <p class="text-h6 font-weight-medium mb-4">Color</p>
     <v-row>
      <v-col cols="12" sm="6">
      <v-color-picker
  
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