<script setup lang="ts">
import { useProfessorStore } from '../../stores/index';


interface Props {
  //axis: Plot.Axis;
  professor: App.Professor
}

defineProps<Props>();

const professorStore = useProfessorStore();
const handleUpVoteProfessor = async (professor: App.Professor) => {
    console.log('handleUpVoteProfessor')
    const newProfessorData = {
        ...professor
    }
    newProfessorData.upvotes = newProfessorData.upvotes + 1
    await professorStore.editProfessor(professor._id, professor)
}


const handleDownVoteProfessor = async (professor: App.Professor) => {
    console.log('handleDownVoteProfessor')
    const newProfessorData = {
        ...professor
    }
    newProfessorData.downvotes = newProfessorData.downvotes - 1
    await professorStore.editProfessor(professor._id, professor)
}
</script>

<template>
    <v-img
        class="align-end"
        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
        height="200px"
        :src="professor.image"
        cover
    >
        <v-card-title class="text-white" v-text="professor.name"></v-card-title>
    </v-img>
    <v-card-actions>
        <v-btn
            color="medium-emphasis"
            icon="mdi-comment"
            @click="handleUpVoteProfessor(professor)"
            size="small"
        ></v-btn>
        <v-spacer></v-spacer>
        {{professor.upvotes }}
        <v-btn
            color="medium-emphasis"
            icon="mdi-thumb-up-outline"
            @click="handleDownVoteProfessor(professor)"
            size="small"
        ></v-btn>
        {{professor.downvotes }}
        <v-btn
            color="medium-emphasis"
            icon="mdi-thumb-down-outline"
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