<script setup lang="ts">
import { useWellStore } from '@/stores';

import { onMounted, Ref, ref } from 'vue';

const wellLogsFilterTableHeader = [
        {
          title: 'Name',
          align: 'start',
          key: 'name',
          sortable: false,
          removable: false,
        },
        { title: 'Creation time', key: 'create_time', removable: false },
]



const wellStore = useWellStore()
interface WellInfo {
    create_time: String,
    name: String
}



const tableWellInfo: Ref<WellInfo[]> = ref([])
const populateTableWellInfo = () => {
    tableWellInfo.value = wellStore.wells.forEach((well) => {
        return {name: well.name, create_time: well.create_time}
    })
    tableWellInfo.value = [{name: "355RJS", create_time: "2022-01-01"}, {name: "342", create_time: "2022-01-01"}, {name: "355RJS", create_time: "2022-01-01"}]
}


onMounted(() => {
   populateTableWellInfo()
})
</script>

<template>
     <v-data-table
            class="mt-10 mb-10"
            :headers="wellLogsFilterTableHeader"
            :items="tableWellInfo"
            disable-pagination
            hide-default-footer
        >
   
        
    </v-data-table>
</template>

<style lang="scss" scoped>

</style>