<script setup lang="ts">
import { useDialogStore } from '@/stores';



const props = defineProps({
    /** Vuetify Card Title name */
    cardTitle: {
        type: String,
        required: true
    }
})


const dialogStore = useDialogStore()

</script>

<template>
    <v-container class="d-flex flex-column  justify-center">
 
    <v-dialog :model-value="dialogStore.shouldOpenDialog" max-width="600px" persistent>
        <v-container class="d-flex flex-column align-center justify-center">
            <v-card class="auth-card">
                <v-card-title class="grey lighten-2">{{  props.cardTitle }}</v-card-title>
                <v-card-text>
                    <slot></slot>
                </v-card-text>
            </v-card>
        </v-container>
   
    
    </v-dialog>
       </v-container>
</template>

<style scoped>
.auth-card {
  max-width: 800px;
  width: 100%;
  border-radius: 12px;
  overflow: hidden;
}
</style>