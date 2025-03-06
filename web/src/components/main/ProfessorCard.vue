<script setup lang="ts">
import { useProfessorStore } from '../../stores/index';

const professorStore = useProfessorStore();
</script>

<template>
    <v-img
        class="align-end"
        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
        height="200px"
        cover
    >
        <v-card-title class="text-white" v-text="'Joao Vitor O brabo'"></v-card-title>
    </v-img>
    <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
            color="medium-emphasis"
            icon="mdi-heart"
            size="small"
        ></v-btn>

        <v-btn
            color="medium-emphasis"
            icon="mdi-bookmark"
            size="small"
        ></v-btn>

        <v-btn
            color="medium-emphasis"
            icon="mdi-share-variant"
            size="small"
        ></v-btn>
    </v-card-actions>
</template>

<style scoped>

</style>