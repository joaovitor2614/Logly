<script setup lang="ts">
import {onBeforeMount, ref, Ref} from 'vue'
import { getParsedWellLogByID } from '@/utils/well';
import { useRoute } from 'vue-router';


const route = useRoute()
const currentWellLogData: Ref<Number[]> = ref([])
const setWellLogDataToDisplay = await () => {
    const params = route.params
    console.log('params', params)
    //const wellID, wellLogID = dataFetchIDS.split("/");
    //currentWellLogData.value = await getParsedWellLogByID(wellLogID, wellID)
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