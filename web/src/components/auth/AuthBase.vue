<script setup lang="ts">
const props = defineProps({
    /** Vuetify Card Title name */
    helperTitle: {
        type: String,
        required: true
    }
})
</script>

<template>

        <v-container fluid class="d-flex justify-center fill-height bg-grey-lighten-3 text-center" >
            <v-card elevation="4" class="auth-card pa-10" min-width="50vh">
                
                <v-card-title class="grey lighten-2 mb-10">{{  props.helperTitle }}</v-card-title>
                <v-card-text class="mt-8">
                     <slot></slot>
                </v-card-text>
               
            </v-card>
          

       </v-container>
</template>

<style scoped>
.auth-card {


  border-radius: 12px;
  overflow: hidden;
}
</style>