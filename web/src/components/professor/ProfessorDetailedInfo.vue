<template>
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
</template>

  <script setup lang="ts">
import { onBeforeMount } from 'vue';
import { useProfessorStore } from '../../stores';
import { ref } from 'vue';

const props = defineProps<{ id: string }>()
  // No reactive data needed for this static component

const professorStore = useProfessorStore();


const professorInfo: App.Professor = ref({})

const setCurrentProfessorInfo = () => {
  professorInfo.value = professorStore.professorCollection.find(professor => professor._id === props.id)
  console.log('professorInfo.value', professorInfo.value)
}

onBeforeMount(() => {
    setCurrentProfessorInfo()
  })
</script>
  
<style scoped>
  .profile-card {
    max-width: 800px;
    margin: auto;
  }
  
  .metric {
    display: flex;
    flex-direction: column;
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
  
  .metric-label {
    font-size: 0.85rem;
    color: #666;
  }
  </style>