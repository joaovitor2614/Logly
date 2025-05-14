<script setup lang="ts">
import Button from '@/components/common/Button.vue'
import { computed } from 'vue';
import { useUserStore } from '../../stores/index';
import UploadService from '../common/UploadService.vue'
import useForm from '../../hooks/useForm';



const userStore = useUserStore()

const {form, errorsMessage, formFieldsInvalidState } = useForm()




const setDefaultFormValues = () => {
    
    form.email = userStore.userInfo.email
    form.name = userStore.userInfo.name
    form.image = userStore.userInfo.image
}

const isDisabled = computed(() => 
    formFieldsInvalidState.value['email'] 
    || formFieldsInvalidState.value['name']
    ? true : false
);

setDefaultFormValues()

const editUserInfo = () => {

    userStore.editUserInfo({name: form.name, image: form.image})
}

</script>

<template>
    <v-container fluid class="d-flex align-center justify-center fill-height">
            <v-row justify="center">
                <v-col cols="10" sm="4">
                    <v-card class="pa-4" elevation="2">
                    
                        <v-card-text>
                            <v-row >
                                <v-col cols="12" align="center" justify="center">

                                    <UploadService v-model:image="form.image"/>
                                </v-col>
                            </v-row>
                            <v-row class="d-flex justify-start align-center">
                                    <v-text-field
                                        v-model="form.name"
                                        name="Name"
                                        label="Name"
                                        type="text"
                                        placeholder="Name"
                                        required
                                    ></v-text-field>
                            </v-row>
                            <v-row class="d-flex justify-start align-center">
                                    <v-text-field
                                        v-model="form.email"
                                        :disabled="true"
                                        name="email"
                                        label="Email"
                                        type="email"
                                        placeholder="Email"
                                        required
                                    ></v-text-field>

                            </v-row>

                            <v-row class="d-flex justify-start align-center">
                                <Button
                                    :buttonAction="editUserInfo" 
                                    :isDisabled="isDisabled" 
                                >
                                    Edit

                                </Button>
                            </v-row>
                              
                       
                        </v-card-text>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
</template>

<style scoped>

</style>