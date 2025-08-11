<script setup lang="ts">
import { useWellStore } from '@/stores';

import { computed } from 'vue';

const wellLogsFilterTableHeader = [
        {
          title: 'Name',
          key: 'name',
          sortable: false,
          removable: false,
        },
        { title: 'Creation time', key: 'create_time', removable: false },
        { title: 'Actions', key: 'id', removable: false },
]



const wellStore = useWellStore()


const tableWellInfo = computed(() => wellStore.wells.map((wellInfo) => {
    return { name: wellInfo.name, create_time: wellInfo.create_time, id: wellInfo._id }
}))



const deleteWell = (id: string) => {
    wellStore.deleteWell(id)

}


</script>

<template>
     <v-data-table
            class="mt-10 mb-10"
            :headers="wellLogsFilterTableHeader"
            :items="tableWellInfo"
            :id="'test-well-table'"
            disable-pagination
            hide-default-footer
        >
        <template v-slot:item.id="{ item }">
            <v-btn
            icon
            @click="deleteWell(item.id)"
            variant="text"
            style="color: black"
        >
            <v-icon >mdi-delete</v-icon>
            </v-btn>
        </template>

   
        
    </v-data-table>
</template>

<style lang="scss" scoped>

</style>