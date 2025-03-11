<script setup>
import { computed } from 'vue'
import ProfessorCard from './ProfessorCard.vue'
import { useProfessorStore } from '../../stores/index';

const professorStore = useProfessorStore();



</script>

<template>
    <v-container fluid>
        <v-row>

             <v-col v-for="(professor, i) in professorStore.professorFilteredCollection.slice(0, 6)"
                :key="i"
                cols="12"
                md="4"
              >
                <ProfessorCard :professor="professor" />
            </v-col>
        </v-row>
    </v-container>
</template>

<style lang="scss" scoped>

</style>