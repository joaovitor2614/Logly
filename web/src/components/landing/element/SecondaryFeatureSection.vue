<template>
  <v-container class="py-16">
    <v-row align="center" justify="center" class="flex-column-reverse flex-md-row">
      <!-- Left Content -->
      <v-col cols="12" md="6">
        <h2 class="text-h4 text-md-h3 font-weight-bold mb-4">
          Well Log Visualization Tools
        </h2>
        <p class="text-body-1 text-medium-emphasis mb-6">
          Our platform provides  visualization capabilities designed specifically
          for geophysical data interpretation. Logly delivers the tools geoscientists need.
        </p>

        <ul class="feature-list">
          <li>LAS 2.0 Well file import</li>
          <li>Well Log Visualization</li>
          <li>Well Data Visualization </li>
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