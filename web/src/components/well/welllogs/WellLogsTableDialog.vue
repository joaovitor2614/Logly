<script setup lang="ts">
import Button from '@/components/common/Button.vue';
import DialogWrapper from '@/components/common/DialogWrapper.vue';
import { useDialogStore, useWellStore } from '@/stores'
import { computed } from 'vue'

interface Props {
    wellID: string
}

const props = defineProps<Props>()

const wellStore = useWellStore()
const dialogStore = useDialogStore();

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

const tableWellLogsInfo = computed(() => {
    const wellLogsInfo = []
    const wellInfo = wellStore.wells.find(well => well._id == props.wellID)
    if (wellInfo) {
        wellInfo.welllogs.forEach(wellLog => {
            wellLogsInfo.push({ name: wellLog.name, unit: wellLog.unit, description: wellLog.description, id: wellLog._id })
        })
    }
    return wellLogsInfo
})

const deleteWellLog = (welllogID: string) => {
    console.log('click icon', props.wellID, welllogID)
    wellStore.deleteWellLog(props.wellID, welllogID)
}


</script>

<template>
    <DialogWrapper :cardTitle="'Well Logs Table'">
        <v-container class="d-flex flex-column justify-center pa-12">
            <v-data-table
                    class="mt-2 mb-10"
                    :headers="wellLogsFilterTableHeader"
                    :items="tableWellLogsInfo"
                    :id="'test-well-table'"
                 
                    hide-default-footer
                >
                <template v-slot:item.id="{ item }">
                    <v-btn
                    icon
                    @click="deleteWellLog(item.id)"
                    variant="text"
                    style="color: black"
                >
                    <v-icon >mdi-delete</v-icon>
                    </v-btn>
                </template>

        
                
            </v-data-table>
            <v-card-actions>
                <Button 
                :id="'test-well-logs-table-ancel-btn'"
                :buttonAction="dialogStore.closeDialogWindow"
                >
                    Close
                </Button>  
            </v-card-actions> 

        </v-container>
    </DialogWrapper>
    

</template>

<style lang="scss" scoped>

</style>