<script setup lang="ts">
import { reactive } from 'vue';
import { useUserStore } from '../../stores/index';
import UploadService from '../common/UploadService.vue'



const userStore = useUserStore()

const userInfo = reactive(userStore.userInfo)

</script>

<template>
    <v-container fluid class="d-flex align-center justify-center fill-height">
            <v-row justify="center">
                <v-col cols="12" sm="8">
                    <v-card>
                    
                        <v-card-text>
                            <v-row >
                                <v-col cols="12" align="center" justify="center">
                                    <UploadService v-model:image="userInfo.image"/>
                                </v-col>
                            </v-row>
                            <v-row >
                                <v-col cols="6">
                                    <v-text-field
                                        v-model="userInfo.name"
                                        name="Name"
                                        label="Name"
                                        type="text"
                                        placeholder="Name"
                                        required
                                    ></v-text-field>
                                </v-col>
                                <v-col cols="6">
                                    <v-text-field
                                        v-model="userInfo.email"
                                        name="email"
                                        label="Email"
                                        type="email"
                                        placeholder="Email"
                                        required
                                    ></v-text-field>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col cols="6">
                                    <v-text-field
                                        name="Phone"
                                        label="Phone"
                                        type="text"
                                        placeholder="Phone"
                                        required
                                    ></v-text-field>
                                </v-col>
  
                            </v-row>
                            <v-card-actions>
                                <v-btn>Edit</v-btn>
                            </v-card-actions>
                        </v-card-text>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
</template>

<style scoped>

</style>