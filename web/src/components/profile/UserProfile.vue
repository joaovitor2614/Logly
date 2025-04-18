<script setup lang="ts">
import { reactive } from 'vue';
import { useUserStore } from '../../stores/index';
import UploadService from '../common/UploadService.vue'
import useForm from '../../hooks/useForm';



const userStore = useUserStore()

const {form, errors} = useForm()

console.log('uasusa', userStore.userInfo)


const setDefaultFormValues = () => {
    
    form.email = userStore.userInfo.email
    form.username = userStore.userInfo.name
    form.image = userStore.userInfo.image
}

setDefaultFormValues()

const editUserInfo = () => {

    userStore.editUserInfo({name: form.username, image: form.image})
}

</script>

<template>
    <v-container fluid class="d-flex align-center justify-center fill-height">
            <v-row justify="center">
                <v-col cols="12" sm="8">
                    <v-card>
                    
                        <v-card-text>
                            <v-row >
                                <v-col cols="12" align="center" justify="center">

                                    <UploadService v-model:image="form.image" :value="userStore.userInfo.image"/>
                                </v-col>
                            </v-row>
                            <v-row >
                                <v-col cols="6">
                                    <v-text-field
                                        v-model="form.username"
                                        :value="userStore.userInfo.name"
                                        name="Name"
                                        label="Name"
                                        type="text"
                                        placeholder="Name"
                                        required
                                    ></v-text-field>
                                </v-col>
                                <v-col cols="6">
                                    <v-text-field
                                        v-model="form.email"
                                        :value="userStore.userInfo.email"
                                        :disabled="true"
                                        name="email"
                                        label="Email"
                                        type="email"
                                        placeholder="Email"
                                        required
                                    ></v-text-field>
                                </v-col>
                            </v-row>

                            <v-card-actions>
                                <v-btn @click="editUserInfo">Edit</v-btn>
                            </v-card-actions>
                        </v-card-text>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
</template>

<style scoped>

</style>