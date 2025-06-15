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
    <v-dialog :model-value="dialogStore.shouldOpenDialog" max-width="600px" persistent>
    <v-card>
        <v-card-title class="grey lighten-2">{{  props.cardTitle }}</v-card-title>
        <v-card-text>
            <slot></slot>
        </v-card-text>
    </v-card>
    
    </v-dialog>
</template>

<style lang="scss" scoped>

</style>