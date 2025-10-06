<script setup lang="ts">
import {onBeforeMount, ref, Ref} from 'vue'
import { getParsedWellLogByID } from '@/utils/well';
import { useRoute } from 'vue-router';


const route = useRoute()
const currentWellLogData: Ref<Number[]> = ref([])
const setWellLogDataToDisplay = async () => {
    const {well_id, well_log_id } = route.params

 
    currentWellLogData.value = await getParsedWellLogByID(well_log_id, well_id)
    console.log('currentWellLogData.value', currentWellLogData.value)
}

onBeforeMount(() => {
    setWellLogDataToDisplay()

})
</script>

<template>
    <div>

    </div>
</template>

<style scoped>

</style>