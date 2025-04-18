<template>
  <v-container fluid class="d-flex flex-column align-center  justify-center">
    <v-avatar size="225">
      <v-img :src="professorInfo.image" :alt="professorInfo.name" />
    </v-avatar>
    <v-row class="mt-4">
      <v-col cols="12">
        <div class="text-h4 font-weight-bold">{{ professorInfo.name }}</div>
      </v-col>
    </v-row>
    <v-row class="d-flex  align-center  justify-center">
      <div class="mr-4">
        <v-icon
          color="black"
          icon="mdi-thumb-up"

        ></v-icon>
        <span class="metric-label">{{ professorInfo.upvotes.length }}</span>
      
  
      </div>
      <div class="ml-4">
        <v-icon
          color="black"
          icon="mdi-thumb-down"

        ></v-icon>
        <span class="metric-label">{{ professorInfo.downvotes.length }}</span>
      
  
      </div>
    </v-row>

      <v-div class="d-flex align-center justify-center ma-6">
        <div class="mr-6">
          <v-icon
            color="black"
            icon="mdi-phone"

          ></v-icon>
          <span class="text-subtitle-1">{{ professorInfo.phone ? professorInfo.phone : 'Unknown'  }}</span>
        </div>
        <div class="ml-6">
          <v-icon
            color="black"
            :icon="professorGenderByIconName[professorInfo.gender]"

          ></v-icon>
          <span class="text-subtitle-1">{{professorInfo.gender}}</span>

        </div>
      
      </v-div>



  </v-container>
  <!--
    <v-card class="pa-6 d-flex align-center justify-center rounded-xl profile-card" elevation="2">
    <v-avatar size="96" class="me-6">
      <v-img :src="professorInfo.image" alt="Francisco R. Abrantes Júnior" />
    </v-avatar>
    
    <div class="flex-grow-1">
      <div class="text-h6 font-weight-bold">{{ professorInfo.name }}</div>
      <div class="text-subtitle-2 text-grey-darken-1 mb-1">
        PhD · Professor at Fluminense Federal University
      </div>
      <div class="text-body-2 text-grey-darken-1 mb-4">Brazil</div>

      <div class="d-flex flex-wrap gap-4">
        <div class="metric">
          <span class="metric-value">{{ professorInfo.upvotes.length }}</span>
          <span class="metric-label">Upvotes</span>
        </div>
        <div class="metric">
          <span class="metric-value">{{ professorInfo.downvotes.length }}</span>
          <span class="metric-label">DownVotes</span>
        </div>
    
      </div>
    </div>
  </v-card>
  -->
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