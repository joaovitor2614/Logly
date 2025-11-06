<script setup lang="ts">
import Button from '@/components/common/Button.vue';
import DialogWrapper from '@/components/common/DialogWrapper.vue';
import { useDialogStore, useWellStore } from '@/stores'
import { computed } from 'vue'
import { useRouter } from 'vue-router';

type TableWellLogsInfo = Pick<App.Well.WellLog, "name" | "unit" | "description" | "_id">[]
interface Props {
    wellID: string,
    localWellLogsInfo: TableWellLogsInfo
}

const props = withDefaults(defineProps<Props>(),{
    localWellLogsInfo: [] as unknown as TableWellLogsInfo,
})

const wellStore = useWellStore()
const dialogStore = useDialogStore();
const router = useRouter()

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

const getTableWellLogsInfoFromStore = () => {
    const wellLogsInfo: TableWellLogsInfo = []

    const wellInfo = wellStore.wells.find(well => well._id == props.wellID)
    if (wellInfo) {
        wellInfo.welllogs.forEach(wellLog => {
            wellLogsInfo.push({ name: wellLog.name, unit: wellLog.unit, description: wellLog.description, _id: wellLog._id })
        })
    }
    return wellLogsInfo
}

const tableWellLogsInfo = computed(() => {

    if (!props.localWellLogsInfo.length) {
        return getTableWellLogsInfoFromStore()
    }
    return props.localWellLogsInfo
    
})

const deleteWellLog = (welllogID: string) => {
    wellStore.deleteWellLog(props.wellID, welllogID)
}

const openWellLogDataDisplayPage = (welllogID: string) => {
    router.push(`data/${props.wellID}/${welllogID}`)
    dialogStore.closeDialogWindow()
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
                    @click="deleteWellLog(item._id)"
                    variant="text"
                    style="color: black"
                >
                    <v-icon >mdi-delete</v-icon>
                </v-btn>
                <v-btn
                    icon
                    @click="openWellLogDataDisplayPage(item._id)"
                    variant="text"
                    style="color: black"
                >
                    <v-icon >mdi-eye</v-icon>
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