<script setup lang="ts">
import { computed } from 'vue';
import { useProfessorStore, useUserStore } from '../../../stores/index';
import CommentSection from './comments/CommentSection.vue';
import { ref } from 'vue'
import { router } from '../../../router/router'

interface Props {
  //axis: Plot.Axis;
  professor: App.Professor.Professor
}

const props = defineProps<Props>();

const professorStore = useProfessorStore();
const handleUpVoteProfessor = async (professorID:string) => {
    professorStore.rankProssessor(professorID, 'upvotes')
}


const handleDownVoteProfessor = async (professorID:string) => {
    professorStore.rankProssessor(professorID, 'downvotes')

    //await professorStore.editProfessor(professor._id, newProfessorData)
}

const userStore = useUserStore();

const checkHasVotedProfessor = (feedbackType: 'upvotes' | 'downvotes') => {
   
    return props.professor[feedbackType].some(vote => vote.user_id === userStore.userInfo._id)
}


const hasUserUpVotedProfessor = computed(() => checkHasVotedProfessor('upvotes'))
const hasUserDownVotedProfessor = computed(() => checkHasVotedProfessor('downvotes'));
const upVotesIcon = computed(() => hasUserUpVotedProfessor.value ? 'mdi-thumb-up' : 'mdi-thumb-up-outline')
const downVotesIcon = computed(() => hasUserDownVotedProfessor.value ? 'mdi-thumb-down' : 'mdi-thumb-down-outline')



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
            :icon="upVotesIcon"
            @click="handleUpVoteProfessor(professor._id)"
            size="small"
        ></v-btn>
        {{professor.upvotes.length }}
        <v-btn
            color="medium-emphasis"
            :icon="downVotesIcon"
            @click="handleDownVoteProfessor(professor._id)"
            size="small"
        ></v-btn>
        {{ professor.downvotes.length }}

        <v-btn
            color="medium-emphasis"
            icon="mdi-chevron-right"
            size="small"
            @click="router.push(`/professor/${professor._id}`)"
        ></v-btn>
    </v-card-actions>
    <CommentSection v-if="isShowCommentSection" :comments="professor.comments" :professorID="professor._id" />
</template>

<style scoped>

</style>