<script setup lang="ts">
import { reactive } from 'vue'
import UploadService from '../../common/UploadService.vue'
import { useProfessorStore } from '../../../stores/index'
import  useForm from '../../../hooks/useForm'

const professorStore = useProfessorStore()



const { form, errorsMessages } = useForm

const handleAddProfessor = () => {
    professorStore.addProfessor(form)
}

const undergraduateCourses = [
  "Physics",
  "Geophysics",
  "Geography",
  "Geography",
  "Geography",
  "Technological Degree in Management Processes",
  "History",
  "History)",
  "Journalism",
  "Literature",
  "Computer Science",
  "Information Systems",
  "Mathematics",
  "Biology",
  "Chemistry",
  "Engineering",
  "Environmental Science",
  "Social Sciences",
  "Philosophy",
  "Economics",
  "Law",
  "Pedagogy",
  "Architecture",
  "Medicine",
  "Nursing",
  "Psychology",
  "Business Administration",
  "International Relations",
  "Public Administration"
];


const cancel = () => {
    professorStore.shouldOpenAddProfessorDialog = false
}
</script>

<template>
    <v-dialog :model-value="professorStore.shouldOpenAddProfessorDialog" max-width="600px" persistent>
        <v-container>
            <v-row align="center" justify="center">
                <v-col cols="12" sm="10">
                    <v-card>
                    <v-card-title class="grey lighten-2">Add Professor</v-card-title>
                        <v-card-text>
                            <v-row class="d-flex justify-center algin-center">
                                <v-col cols="12">
                                    <UploadService v-model:image="form.image"/>
                                </v-col>
                            </v-row>
                            <v-row class="d-flex justify-center algin-center" >
                                <v-col cols="6">
                                    <v-text-field
                                        v-model="form.name"
                                        name="Name"
                                        label="Name"
                                        type="text"
                                        placeholder="Name"
                                        required
                                    ></v-text-field>
                                </v-col>
                                <v-col cols="6">
                                    <v-text-field
                                        v-model="form.phone"
                                        name="Phone"
                                        label="Phone"
                                        type="text"
                                        placeholder="Name"
                                        prepend-icon="mdiPhone"
                                        required
                                    ></v-text-field>
                                </v-col>
                            </v-row>
                            <v-row class="d-flex justify-center algin-center">
                                <v-col cols="6">
                                    <v-select
                                        :items="undergraduateCourses"
                        
                                        v-model="form.disciplines"
                                        label="Disciplines"
                                    ></v-select>
                                </v-col>
                            </v-row>
                            <v-card-actions>
                                <v-btn @click="handleAddProfessor()">Add</v-btn>
                                <v-btn @click="cancel">Cancel</v-btn>
                            </v-card-actions>
                        </v-card-text>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>

       
  
    </v-dialog>
</template>

<style scoped>

</style>