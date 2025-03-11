<script setup lang="ts">
import { reactive } from 'vue';
import { useUserStore } from '../../stores/index';




const userStore = useUserStore()

const userInfo = reactive(userStore.userInfo)

</script>

<template>
    <v-container>
            <v-row align="center" justify="center">
                <v-col cols="12" sm="10">
                    <v-card>
                    <v-card-title class="grey lighten-2">Add Professor</v-card-title>
                        <v-card-text>
                            <v-row align="center" justify="center">
                                <v-col cols="12" align="center" justify="center">
                                    <v-avatar size="150">
                                    <v-img
                                        alt="John"
                                        src="https://cdn.vuetifyjs.com/images/john.jpg"
                                    ></v-img>
                                    </v-avatar>
                                </v-col>
                            </v-row>
                            <v-row align="center" justify="center" >
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
                            <v-row align="center" justify="center" >
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