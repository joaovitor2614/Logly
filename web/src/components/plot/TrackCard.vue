<script setup lang="ts">

interface wellLogItemToSelect {
    title: string,
    value: string
}
interface Props {
    wellLogsItemsToSelect: wellLogItemToSelect[],
    trackIndex: number
}
const props = defineProps<Props>()
</script>

<template>
    <div>
        <v-select               
            class="mt-4 mb-3"
            :items="props.wellLogsItemsToSelect"
            :label="`Track ${props.trackIndex}`"

            hide-details
            outlined
            dense
        />
    </div>
</template>

<style scoped>

</style>