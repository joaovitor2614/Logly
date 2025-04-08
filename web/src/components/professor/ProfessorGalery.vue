<script setup>
import { computed } from 'vue'
import ProfessorCard from './card/ProfessorCard.vue'
import { useProfessorStore } from '../../stores/index';
import { ref } from 'vue';

const professorStore = useProfessorStore();
const page = ref(1)
const perPage = 6;

const paginatedProfessors = computed(() => {
    const start = (page.value -1) * perPage;
    return professorStore.finalProfessorCollection.slice(start, start + perPage);
})

</script>

<template>
    <v-container fluid class="d-flex align-center justify-center fill-height">
        <v-row>
    
            <v-col v-for="(professor, i) in paginatedProfessors"
                :key="i"
                cols="12"
                md="4"
            >
                <ProfessorCard :professor="professor" />
            </v-col>
                
        </v-row>
        <v-row class="d-flex align-center justify-center mt-5">
            <v-pagination
                    v-model="page"
                    :length="Math.ceil(professorStore.finalProfessorCollection.length / perPage)"
                    :total-visible="6"
            />
        </v-row>
       
    </v-container>
</template>

<style lang="scss" scoped>

</style>