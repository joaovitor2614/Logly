<script setup>
import { ref } from 'vue';
import AddProfessorDialog from './AddProfessorDialog.vue';


const shouldOpenProfessorDialog = ref(false)

const openProfessorDialog = () => {
    shouldOpenProfessorDialog.value = true;
}
</script>

<template>
    <v-container class="mt-9">
            <AddProfessorDialog v-model:shouldOpenProfessorDialog="shouldOpenProfessorDialog" />
            <v-row align="center" justify="center" >
                <v-col cols="4" sm="10">
                    <v-row align="center" justify="start">
                    <v-btn
                        class="mr-4"
                        color="blue"
                        icon="mdi-plus"
                        size="large"
                        @click="openProfessorDialog"
                    >
                       
                    </v-btn>
                    <h3>Add Professor</h3>
                    </v-row>

                </v-col>
            </v-row>
</v-container>
</template>

<style lang="scss" scoped>

</style>
