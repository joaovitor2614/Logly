<script setup lang="ts">
import { TableWellLogsInfo } from './types'
interface Props {
    wellLogsInfo: TableWellLogsInfo,
    deleteWellLog?: (welllogID: string) => void ,
    openWellLogDataDisplayPage?: (welllogID: string) => void
}

const props = defineProps<Props>()

const wellLogsFilterTableHeader = [
        {
          title: 'Name',
          key: 'name',
          sortable: false,
          removable: false,
        },
        { title: 'Unit', key: 'unit', removable: false },
        { title: 'Description', key: 'description', removable: false },
        { title: 'Actions', key: 'id', removable: false },
]
console.log('props.wellLogsInfo', props.wellLogsInfo)
</script>

<template>
    <v-data-table
        class="mt-2 mb-10"
        :headers="wellLogsFilterTableHeader"
        :items="props.wellLogsInfo"
        :id="'test-well-table'"
        
        hide-default-footer
    >
                <template v-slot:item.id="{ item }">
                <v-btn
                    icon
                    :disabled="!Boolean(item._id)"
                    @click="props.deleteWellLog(item._id)"
                    variant="text"
                    style="color: black"
                >
                    <v-icon >mdi-delete</v-icon>
                </v-btn>
                <v-btn
                    icon
                    @click="props.openWellLogDataDisplayPage(item._id)"
                    :disabled="!Boolean(item._id)"
                    variant="text"
                    style="color: black"
                >
                    <v-icon >mdi-eye</v-icon>
                </v-btn>
                </template>

        
                
    </v-data-table>
</template>

<style scoped>

</style>