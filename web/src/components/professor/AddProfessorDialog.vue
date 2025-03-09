<script setup lang="ts">



const shouldOpenProfessorDialog = defineModel('shouldOpenProfessorDialog', { required: true, type: Boolean })

const cancel = () => {
    shouldOpenProfessorDialog.value = false
}
</script>

<template>
    <v-dialog :model-value="shouldOpenProfessorDialog" max-width="600px" persistent>
        <v-card>
        <v-card-title class="grey lighten-2">Add Professor</v-card-title>
        <v-card-text>
            <h1>Add Professor</h1>
            <v-card-actions>
                <v-btn>Add</v-btn>
                <v-btn @click="cancel">Cancel</v-btn>
            </v-card-actions>
        </v-card-text>
    </v-card>
    </v-dialog>
</template>

<style scoped>

</style>