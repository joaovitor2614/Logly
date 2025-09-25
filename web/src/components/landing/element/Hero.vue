<template>
  <v-container fluid class="hero-container d-flex align-center justify-center">
    <div class="hero-content text-center">
      <h1 class="hero-title">
        Visualize Your <br />
        Geophysical Data
      </h1>
      <p class="hero-subtitle">
        Well log visualization platform geocientists. 
        Analyze subsurface formations with precision and clarity.
      </p>

      <div class="d-flex justify-center mt-6 gap-4">
        <v-btn color="primary" rounded="xl" size="large" class="px-6">
          Start Exploring
        </v-btn>
        <v-btn outlined rounded="xl" size="large" class="px-6">
          Learn More
        </v-btn>
      </div>

      <div class="scroll-indicator mt-12">
        <v-icon size="32">mdi-mouse</v-icon>
      </div>
    </div>
  </v-container>
</template>

<script setup>
// nothing special needed here
</script>

<style scoped>
.hero-container {
  min-height: 100vh;
  background: linear-gradient(
      rgba(0, 0, 0, 0.55),
      rgba(0, 0, 0, 0.55)
    ),
    url('../../../assets/oilandgas.jpg'); /* Replace with your image path */
  background-size: cover;
  background-position: center;
  color: white;
}

.hero-content {
  max-width: 900px;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 700;
  line-height: 1.2;
}

.hero-subtitle {
  font-size: 1.25rem;
  margin-top: 1.5rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.85);
}

.scroll-indicator {
  animation: bounce 2s infinite;
  color: white;
}

@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(10px);
  }
  60% {
    transform: translateY(5px);
  }
}
</style>