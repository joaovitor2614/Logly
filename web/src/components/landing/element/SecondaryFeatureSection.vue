<template>
  <v-container class="py-16">
    <v-row align="center" justify="center" class="flex-column-reverse flex-md-row">
      <!-- Left Content -->
      <v-col cols="12" md="6">
        <h2 class="text-h4 text-md-h3 font-weight-bold mb-4">
          Industry-Leading Visualization Tools
        </h2>
        <p class="text-body-1 text-medium-emphasis mb-6">
          Our platform provides cutting-edge visualization capabilities designed specifically
          for geophysical data interpretation. From basic well logs to complex formation analysis,
          Logly delivers the tools professionals trust.
        </p>

        <ul class="feature-list">
          <li>Real-time data processing and visualization</li>
          <li>Customizable chart types and layouts</li>
          <li>Advanced filtering and correlation tools</li>
          <li>Export-ready professional reports</li>
        </ul>
      </v-col>

      <!-- Right Image -->
      <v-col cols="12" md="6" class="d-flex justify-center">
        <v-card elevation="2" rounded="xl" class="pa-2">
          <v-img
            src="../../../assets/linkedin_logo.png"
            alt="Geophysic well log"
            width="100%"
            max-width="600"
            class="rounded-lg"
            cover
          />
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
// no script logic needed here
</script>

<style scoped>
.feature-list {
  padding-left: 1.5rem;
  list-style-type: disc;
  color: rgba(0, 0, 0, 0.8);
  font-size: 1rem;
  line-height: 1.6;
}
</style>