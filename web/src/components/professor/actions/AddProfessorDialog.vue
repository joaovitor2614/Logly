<script setup lang="ts">
import { reactive } from 'vue'
import UploadService from '../../common/UploadService.vue'
import { useProfessorStore } from '../../../stores/index'

const professorStore = useProfessorStore()


const form = reactive({
    name: '',
    image: ''
})

const handleAddProfessor = () => {
    professorStore.addProfessor(form)
}




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
                          
                            <v-row align="center" justify="center" >
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
                                    <UploadService v-model:image="form.image"/>
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