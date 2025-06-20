<script setup lang="ts">
import DialogWrapper from '@/components/common/DialogWrapper.vue';
import { useWellStore } from '@/stores';
import { Ref, ref } from 'vue';



const wellStore = useWellStore()


const selectedWell: Ref<string> = ref('');

const wellItems = ref([])


const populateWellItems = () => {
    console.log('populateWellItems')
}
</script>

<template>
    <DialogWrapper :cardTitle="'Plot Dialog'">
        <v-row>
            <v-cols cols="10">
                <v-select
                    class="mt-4 mb-3"
                    :items="wellItems"
                    label="Well name"
                    v-model="selectedWell"
                    hide-details
                    outlined
                    dense
                ></v-select>
            </v-cols>
        </v-row>
  
    </DialogWrapper>
</template>

<style scoped>

</style>