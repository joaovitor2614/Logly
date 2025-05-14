<template>
  <v-card class="pa-4" elevation="6" rounded="xl">
    <v-row align="center" justify="space-between" class="flex-wrap">
      <!-- Left: Image -->
      <v-col cols="12" md="3" class="text-center">
        <v-avatar size="120">
          <v-img :src="professorInfo.image" alt="Professor image" />
        </v-avatar>
      </v-col>

      <!-- Center: Name and Votes -->
      <v-col cols="12" md="6" class="text-center">
        <h2 class="text-h5 font-weight-bold mb-2">{{ professorInfo.name }}</h2>
        <v-row align="center" justify="center" dense>
          <v-icon color="success" class="mr-1">mdi-thumb-up</v-icon>
          <span class="mr-4">{{ professorInfo.upvotes.length || 0 }}</span>

          <v-icon color="error" class="mr-1">mdi-thumb-down</v-icon>
          <span>{{ professorInfo.downvotes.length || 0 }}</span>
        </v-row>
      </v-col>

      <!-- Right: Gender and Create Time -->
      <v-col cols="12" md="3" class="text-md-right text-center mt-2 mt-md-0">
        <div class="text-caption grey--text">Gender: {{ professorInfo.gender }}</div>
        <div class="text-caption grey--text">Since: {{ professorInfo.create_time }}</div>
      </v-col>
    </v-row>

    <v-divider class="my-4" />

    <!-- Contact and Disciplines -->
    <v-row>
      <!-- Contact Info -->
      <v-col cols="12" md="6">
        <h3 class="text-subtitle-1 font-weight-medium mb-2">Contact Info</h3>
        <v-list dense>
          <v-list-item>
            <v-list-item-title>
              📞 {{ professorInfo.phone || 'N/A' }}
            </v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>
              📧 {{ 'N/A' }}
            </v-list-item-title>
          </v-list-item>
          <!--
          <v-list-item>
            <v-list-item-title>
              🔗 <a :href="professor.lattes" target="_blank">{{ professor.lattes }}</a>
            </v-list-item-title>
          </v-list-item>
           -->
        </v-list>
       
      </v-col>

      <!-- Disciplines -->
      <v-col cols="12" md="6">
        <h3 class="text-subtitle-1 font-weight-medium mb-2">Disciplines</h3>
        <v-chip-group column>
          <v-chip v-for="(discipline, index) in professorInfo.disciplines" :key="index" class="ma-1" color="primary" variant="tonal">
            {{ discipline }}
          </v-chip>
        </v-chip-group>
      </v-col>
    </v-row>
  </v-card>
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
  .profile-card {
    margin: auto;
    max-width: 800px;
    padding-right: 16px;
    border-right: 1px solid #e0e0e0;
  }

  .metric:last-child {
    border-right: none;
    padding-right: 0;
  }

  .metric-value {
    font-weight: 600;
    font-size: 1.1rem;
    color: #1a1a1a;
  }
  

  .metric {
    display: flex;
    flex-direction: column;
  }
  


  
  .metric-label {
    font-size: 1.25rem;
    color: #666;
  }
  </style>