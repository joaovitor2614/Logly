<script setup>
import { ref } from 'vue';
import { useProfessorStore } from '../../stores/index';

const professorStore = useProfessorStore()

const genderFilterTypes = ['all', 'male', 'female']

</script>

<template>
     <v-container class="mt-6">
            <v-row align="center" justify="center">
                <v-col cols="6">
                    <v-text-field
                        v-model="professorStore.filters.name"
                        name="Name"
                        label="Name"
                        type="text"
                        placeholder="Search by name"
                        append-inner-icon="mdi-magnify"
                        required
                    ></v-text-field>
                </v-col>
                <v-col cols="2">
                    <v-select
                        :items="genderFilterTypes"
         
                        v-model="professorStore.filters.gender"
                        label="Gender"
                    ></v-select>

                </v-col>
            </v-row>
    </v-container>
               
</template>

<style lang="scss" scoped>

</style>
