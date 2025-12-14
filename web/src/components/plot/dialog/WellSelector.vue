<script setup lang="ts">
import { useWellStore } from '@/stores';
import { computed, ModelRef} from 'vue';




const wellID: ModelRef<string | undefined> = defineModel('wellID');

const wellStore = useWellStore()

const wellItems = computed(() => wellStore.wells.map((well) => {
    return { title: well.name, value: well._id }
}))
</script>

<template>
    <v-select               
            class="mt-4 mb-3"
            :items="wellItems"
            label="Well name"
            id="test-selected-wells-to-plot-selector"
            v-model="wellID"
            hide-details
            outlined
            dense
        />
</template>

<style scoped>

</style>