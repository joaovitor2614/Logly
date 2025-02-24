<script setup lang="ts">


</script>

<template>
    <div>
      <v-app height="100%">
        <v-main height="100%">
          <router-view :key="$route.fullPath" />
        </v-main>
      </v-app>
    </div>
</template>

<style scoped>

</style>
