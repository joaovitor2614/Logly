<script setup lang="ts">
import { reactive } from 'vue'
import UploadService from '../../common/UploadService.vue'
import { useProfessorStore } from '../../../stores/index'
import { availableDisciplines } from '../../../constants/professor'
import  useForm from '../../../hooks/useForm'

const professorStore = useProfessorStore()



const { form, errorsMessages } = useForm()

const handleAddProfessor = () => {
    professorStore.addProfessor(form)
}



const cancel = () => {
    professorStore.shouldOpenAddProfessorDialog = false
}


</script>

<template>
    <v-dialog :model-value="professorStore.shouldOpenAddProfessorDialog" max-width="800px" persistent>
        <v-container fluid class="d-flex align-center justify-center fill-height">
           
                    <v-card width="100%" max-width="80vh" class="pa-6">
                    <v-card-title class="grey lighten-2">Add Professor</v-card-title>
                        <v-card-text>
                            <v-row class="d-flex justify-center algin-center">
                                <v-col cols="12">
                                    <UploadService v-model:image="form.image"/>
                                </v-col>
                            </v-row>
                            <v-row class="d-flex justify-start algin-center" >
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
                            <v-row class="d-flex justify-start algin-center">
                                <v-col cols="6">
                                    <v-select
                                        :items="availableDisciplines"
                                        multiple
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
             
        </v-container>

       
  
    </v-dialog>
</template>

<style scoped>

</style>