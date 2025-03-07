<script setup lang="ts">
interface Props {
  //axis: Plot.Axis;
  professor: App.Professor
}

defineProps<Props>();
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
            size="small"
        ></v-btn>
        <v-spacer></v-spacer>
        {{professor.upvotes }}
        <v-btn
            color="medium-emphasis"
            icon="mdi-thumb-up-outline"
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