vue3<script setup>
import WellSelector from '@/components/well/helpers/WellSelector.vue';
import DialogWrapper from '@/components/common/DialogWrapper.vue';

import {  reactive } from 'vue';

const form = reactive({
    wellID: ''
})
</script>

<template>
    <DialogWrapper :cardTitle="'Well Calculator'">
        <v-container class="d-flex flex-column justify-center pa-12">
            <WellSelector v-model:wellID="form.wellID" />
        </v-container>

   
          
     
    </DialogWrapper>
</template>

<style lang="scss" scoped>

</style>