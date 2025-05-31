<script setup lang="ts">

</script>

<template>
    <v-card>
        <v-card-title class="grey lighten-2">Import</v-card-title>
        <v-card-text>
            <v-row>
                <v-col cols="6">
                    <v-text-field 
                    type="text" 
                    label="LAS File" 
           
                    append-inner-icon="mdi-folder-open" 
                    />
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="6">
                    <v-text-field 
                    type="text" 
                    label="Well name" 
           
         
                    />
                </v-col>
            </v-row>
        </v-card-text>
    </v-card>
</template>

<style scoped>

</style>