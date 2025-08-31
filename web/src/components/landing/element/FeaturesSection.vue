<template>
  <v-container class="py-16">
    <!-- Section Title -->
    <div class="text-center mb-12">
      <h2 class="text-h3 font-weight-bold">
        Powerful Features for Professional Analysis
      </h2>
      <p class="text-body-1 mt-4 text-medium-emphasis">
        Everything you need to visualize, analyze, and interpret geophysical 
        well log data with confidence.
      </p>
    </div>

    <!-- Features Grid -->
    <v-row align="stretch" justify="center" dense>
      <v-col
        v-for="(feature, index) in features"
        :key="index"
        cols="12"
        sm="6"
        md="3"
      >
        <v-card class="pa-6 text-center" elevation="0" rounded="xl">
          <div class="mb-4">
            <v-icon size="48" :color="feature.color">{{ feature.icon }}</v-icon>
          </div>
          <h3 class="text-h6 font-weight-bold">{{ feature.title }}</h3>
          <p class="text-body-2 mt-2 text-medium-emphasis">
            {{ feature.description }}
          </p>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
const features = [
  {
    title: "Advanced Data Visualization",
    description:
      "Interactive charts and graphs for comprehensive well log analysis with real-time data processing.",
    icon: "mdi-chart-line",
    color: "primary",
  },
  {
    title: "Multi-Format Support",
    description:
      "Import and export data in LAS, DLIS, and other industry-standard formats seamlessly.",
    icon: "mdi-folder",
    color: "amber-darken-2",
  },
  {
    title: "Collaborative Platform",
    description:
      "Share insights and collaborate with your team in real-time across multiple projects.",
    icon: "mdi-account-group",
    color: "deep-purple-accent-4",
  },
  {
    title: "Cloud Integration",
    description:
      "Secure cloud storage with automated backup and synchronization across devices.",
    icon: "mdi-cloud",
    color: "indigo",
  },
];
</script>

<style scoped>
.v-card {
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.v-card:hover {
  transform: translateY(-6px);
  box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.15);
}
</style>