<script setup>
import ProfessorCard from './ProfessorCard.vue'
</script>

<template>
    <v-container fluid>
        <v-row>
            <v-col
                v-for="i in 6"
                :key="i"
                cols="12"
                md="4"
              >
                <ProfessorCard />
            </v-col>
        </v-row>
    </v-container>
</template>

<style lang="scss" scoped>

</style>