<template>
  <v-container  fluid class="bg-grey-lighten-3">


  <v-card class="mx-auto" max-width="800" elevation="4">
    <v-card-title class="text-h5 font-weight-bold">
      {{ professorInfo.name }}
      <v-chip class="ml-2" small>
        {{ professorInfo.gender }}
      </v-chip>
    </v-card-title>

    <v-divider></v-divider>

    <v-card-text>
      <v-row>
        <!-- Left Column - Image -->
        <v-col cols="12" md="4" class="text-center">
          <v-avatar size="200" class="elevation-4">
            <v-img
              :src="professorInfo.image"
              alt="Professor photo"
              aspect-ratio="1"
            ></v-img>
          </v-avatar>
        </v-col>

        <!-- Right Column - Details -->
        <v-col cols="12" md="8">
          <!-- Contact Information -->
          <v-list dense class="transparent">
            <v-list-item v-if="professorInfo.phone">
              <v-list-item-icon>
                <v-icon>mdi-phone</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>{{ professorInfo.phone }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item v-if="professorInfo.email">
              <v-list-item-icon>
                <v-icon color="primary">mdi-email</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>{{ professorInfo.email }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>

          </v-list>

          <!-- Disciplines -->
          <v-divider class="my-4"></v-divider>
          <div class="text-subtitle-1 mb-2">Disciplinas</div>
          <v-chip-group>
            <v-chip
              v-for="(discipline, index) in professorInfo.disciplines"
              :key="index"
              class="ma-1"
              outlined
            >
              {{ discipline }}
            </v-chip>
          </v-chip-group>
        </v-col>
      </v-row>
    </v-card-text>

    <!-- Voting Section -->
    <v-card-actions class="px-4 pb-4">
      <v-btn outlined>
        <v-icon left>mdi-thumb-up</v-icon>
        {{ professorInfo.upvotes.length }}
      </v-btn>
      <v-btn  outlined class="ml-2">
        <v-icon left>mdi-thumb-down</v-icon>
        {{ professorInfo.downvotes.length }}
      </v-btn>
    </v-card-actions>
  </v-card>
    </v-container>
</template>


<script setup lang="ts">
import { onBeforeMount } from 'vue';
import { useProfessorStore } from '../../stores';
import { ref } from 'vue';

const props = defineProps<{ id: string }>()
  // No reactive data needed for this static component

const professorStore = useProfessorStore();


const professorInfo: App.Professor = ref({})

const professorGenderByIconName = {
  male: 'mdi-gender-male',
  female: 'mdi-gender-female',
  other: "mdi-robot"
}


const setCurrentProfessorInfo = () => {
  professorInfo.value = professorStore.professorCollection.find(professor => professor._id === props.id)

  
}

onBeforeMount(() => {
    setCurrentProfessorInfo()
  })
</script>
  
<style scoped>
.v-card {
  border-radius: 12px;
  transition: transform 0.3s ease;
}

.v-card:hover {
  transform: translateY(-2px);
}

.primary--text {
  color: #1976d2 !important;
}

.secondary {
  background-color: #26a69a !important;
}
  </style>