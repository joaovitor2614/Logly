<script setup lang="ts">
import Button from '@/components/common/Button.vue';
import DialogWrapper from '@/components/common/DialogWrapper.vue';
import { useDialogStore, useWellStore } from '@/stores'
import { computed } from 'vue'
import { useRouter } from 'vue-router';
import { TableWellLogsInfo } from './types';
import WellLogsTable from './WellLogsTable.vue';

interface Props {
    wellID: string,
}

const props = defineProps<Props>();

const wellStore = useWellStore()
const dialogStore = useDialogStore();
const router = useRouter()



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
        return getTableWellLogsInfoFromStore()
    
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
            <WellLogsTable 
                :wellLogsInfo="tableWellLogsInfo" 
                :deleteWellLog="deleteWellLog" 
                :openWellLogDataDisplayPage="openWellLogDataDisplayPage"
            />
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