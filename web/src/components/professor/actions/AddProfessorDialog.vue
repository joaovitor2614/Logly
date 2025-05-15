<script setup lang="ts">
import Button from '@/components/common/Button.vue'
import UploadService from '../../common/UploadService.vue'
import { useProfessorStore } from '../../../stores/index'
import { availableDisciplines } from '../../../constants/disciplines/index'
import  useForm from '../../../hooks/useForm'
import { computed } from 'vue'

const professorStore = useProfessorStore()



const { form, errorsMessages, formFieldsInvalidState } = useForm()

const handleAddProfessor = () => {
    const hasErrors = professorStore.addProfessor(form)
    if (!hasErrors) {
        professorStore.shouldOpenAddProfessorDialog = false;
    }
}

const genderItems: App.Professor.Gender[] = ['male', 'female', 'other']



const cancel = () => {
    professorStore.shouldOpenAddProfessorDialog = false
}

const genderItemByIconMapping: Record<App.Professor.Gender, string> = {
    'male': 'mdi-gender-male',
    'female': 'mdi-gender-female',
    'other': 'mdi-robot'

}
const currentGenderIcon = computed(() => {
    return genderItemByIconMapping[form.gender]
})

const isDisabled = computed(() => 
formFieldsInvalidState.value['name'] 
|| formFieldsInvalidState.value['disciplines']
|| formFieldsInvalidState.value['phone'] ? true : false
)
console.log('isDisabled', isDisabled)
</script>

<template>
    <v-dialog :model-value="professorStore.shouldOpenAddProfessorDialog" max-width="800px" persistent>
        <v-container fluid class="d-flex align-center justify-center fill-height">
           
                    <v-card width="100%" max-width="80vh" class="pa-6">
                    <v-card-title >Add Professor</v-card-title>
                        <v-card-text>
                            <v-row class="d-flex justify-center align-center">
                                <v-col cols="4">
                                    <UploadService v-model:image="form.image"/>
                                </v-col>
                            </v-row>
                            <v-row class="d-flex justify-start align-center" >
                                <v-col cols="6">
                                    <v-text-field
                                        v-model="form.name"
                                        :error-messages="errorsMessages.name"
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
                                        :error-messages="errorsMessages.phone"
                                        name="Phone"
                                        label="Phone"
                                        type="number"
                                        :prepend-inner-icon="'mdi-phone'"
                                        placeholder="Name"
                                        prepend-icon="mdiPhone"
                                        required
                                    ></v-text-field>
                                </v-col>
                            </v-row>
                            <v-row class="d-flex justify-start align-center">
                                <v-col cols="6">
                                    <v-select
                                        :items="availableDisciplines"
                                        multiple
                                        v-model="form.disciplines"
                                        :error-messages="errorsMessages.disciplines"
                                        label="Disciplines"
                                    ></v-select>
                                </v-col>
                                <v-col cols="6">
                                    <v-select
                                        :items="genderItems"
                                        :prepend-inner-icon="currentGenderIcon"                                     
                                        v-model="form.gender"
                                        label="Gender"
                                    ></v-select>
                                </v-col>
                            </v-row>
            
                            <v-row class="d-flex justify-start align-center">
                                
                                
                                <Button :buttonAction="cancel" class="mr-4">Cancel</Button>
                                <Button :buttonAction="handleAddProfessor" :disabled="isDisabled">Add</Button>
                            </v-row>
                        </v-card-text>
                    </v-card>
             
        </v-container>

       
  
    </v-dialog>
</template>

<style scoped>

</style>