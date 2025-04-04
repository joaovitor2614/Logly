<script setup>
import { computed } from 'vue'
import ProfessorCard from './card/ProfessorCard.vue'
import { useProfessorStore } from '../../stores/index';
import { ref } from 'vue';

const professorStore = useProfessorStore();
const page = ref(1)


</script>

<template>
    <v-container fluid>
        <v-row>
            <v-pagination
                v-model="page"
                :length="20"
                :total-visible="6"
            >
                    <v-col v-for="(professor, i) in professorStore.professorFilteredCollection"
                    :key="i"
                    cols="12"
                    md="4"
                    >
                    <ProfessorCard :professor="professor" />
                    </v-col>

            </v-pagination>

        </v-row>
    </v-container>
</template>

<style lang="scss" scoped>

</style>