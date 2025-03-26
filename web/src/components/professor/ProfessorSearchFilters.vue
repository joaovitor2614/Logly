<script setup>
import { ref } from 'vue';
import { useProfessorStore } from '../../stores/index';

const professorStore = useProfessorStore()



</script>

<template>
     <v-container class="mt-6">
            <v-row align="center" justify="center">
                <v-col cols="4" sm="10">
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
            </v-row>
    </v-container>
               
</template>

<style lang="scss" scoped>

</style>
