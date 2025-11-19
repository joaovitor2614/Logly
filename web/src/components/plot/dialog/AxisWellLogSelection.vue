<script setup lang="ts">

interface WellLogItem {
    title: string,
    value: string
}
interface Props {
    axisName: string,
    wellLogItems: WellLogItem[]
}

const props = withDefaultsdefineProps<Props>();
const wellLogID = defineModel('wellLogID', { required: true, type: String })
</script>

<template>
    <p class="mb-5 mt-5 text-center">{{ props.axisName }}-Axis</p>
    <v-divider></v-divider>
    <v-select
        class="mt-4"
        :items="props.wellLogItems"
        label="Well log name"
        v-model="wellLogID"
        hide-details
        outlined
        dense
    ></v-select>
</template>

<style lang="scss" scoped>

</style>