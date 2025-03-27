<script setup lang="ts">
import { useProfessorStore } from '../../../stores/index';
import CommentSection from './comments/CommentSection.vue';
import { ref } from 'vue'

interface Props {
  //axis: Plot.Axis;
  professor: App.Professor.Professor
}

defineProps<Props>();

const professorStore = useProfessorStore();
const handleUpVoteProfessor = async () => {
    console.log('handleUpVoteProfessor')
}


const handleDownVoteProfessor = async () => {
  
    console.log('handleDownVoteProfessor')
  
    //await professorStore.editProfessor(professor._id, newProfessorData)
}

const isShowCommentSection = ref(false)
const toggleIsShowCommentSection = () => {
    isShowCommentSection.value = !isShowCommentSection.value
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
            @click="toggleIsShowCommentSection()"
            size="small"
        ></v-btn>
        <v-spacer></v-spacer>

        <v-btn
            color="medium-emphasis"
            icon="mdi-thumb-up-outline"
            @click="handleUpVoteProfessor()"
            size="small"
        ></v-btn>
        {{professor.upvotes.length }}
        <v-btn
            color="medium-emphasis"
            icon="mdi-thumb-down-outline"
            @click="handleDownVoteProfessor()"
            size="small"
        ></v-btn>
        {{ professor.downvotes.length }}

        <v-btn
            color="medium-emphasis"
            icon="mdi-share-variant"
            size="small"
        ></v-btn>
    </v-card-actions>
    <CommentSection v-if="isShowCommentSection" :comments="professor.comments" />
</template>

<style scoped>

</style>