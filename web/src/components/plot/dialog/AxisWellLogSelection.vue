<script setup lang="ts">
import { useWellStore } from '@/stores';
import { ModelRef, watch } from 'vue';


interface WellLogItem {
    title: string,
    value: string
}
interface Props {
    axisName: string,
    wellID: string,
    wellLogItems: WellLogItem[]
}

const props = defineProps<Props>();
const wellLogAxis: ModelRef<App.Plot.AxisTemplate> = defineModel('wellLogAxis');

const wellStore = useWellStore()
watch(() => wellLogAxis.value.id, (wellLogID) => {
    if (wellLogID) {
        populateAxesDefaultLimits()
    }
})
const populateAxesDefaultLimits = () => {
    const wellInfo = wellStore.wells.find(well => well._id === props.wellID)
    const wellLogInfo = wellInfo?.welllogs.find(wellLog => wellLog._id === wellLogAxis.value.id)
    if (wellLogInfo) {
        wellLogAxis.value.range = [wellLogInfo.min_value, wellLogInfo.max_value]
    }
}
</script>

<template>
    <p class="mb-5 mt-5 text-center">{{ props.axisName }}-Axis</p>
    <v-divider></v-divider>
    <v-select
        class="mt-4"
        :id="`test-welllog-to-plot-selector`"
        :items="props.wellLogItems"
        label="Well log name"
        v-model="wellLogAxis.id"
        hide-details
        outlined
        dense
    ></v-select>
    <v-row class="d-flex align-center justify-center mt-8 mb-8" v-if="wellLogAxis.id">
        <v-col cols="6">
            <v-text-field
                v-model="wellLogAxis.range[0]"
                label="Min Value"
                type="number"
            />
        </v-col>
          <v-col cols="6">
            <v-text-field
                v-model="wellLogAxis.range[1]"
                label="Min Value"
                type="number"
            />
        </v-col>
    </v-row>
</template>

<style lang="scss" scoped>

</style>