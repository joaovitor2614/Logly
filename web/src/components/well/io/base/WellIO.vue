vue<script setup lang="ts">
import { reactive, Ref, ref } from 'vue';
import useVuelidate from '@vuelidate/core';
import { required} from '@vuelidate/validators'
import { computed } from 'vue';
import Button from '@/components/common/Button.vue'
import DialogWrapper from '../../common/DialogWrapper.vue';
import { useDialogStore, useWellStore } from '@/stores';
import { WellIOTypes } from '../types';

interface Props {
    wellIOType: `${WellIOTypes}`
}

const props = defineProps<Props>();

interface Form {
    lasFile: undefined | File
    wellID: string | undefined
}
const form: Form = reactive({
    lasFile: undefined,
    wellID: undefined
})


const isLoading: Ref<boolean> = ref(false)
const dialogStore = useDialogStore()
const wellStore = useWellStore();


const isImport = computed(() => props.wellIOType == WellIOTypes.Import)

</script>

<template>
    <DialogWrapper :cardTitle="`${wellIOType == isImport : 'Export'} Well`">
        <v-row v-if="isImport">
                    <v-col cols="10">
                        <v-file-input
               
                            v-model="form.lasFile"
                            label="LAS File"
                        ></v-file-input>
               
                    </v-col>
        </v-row>        
    </DialogWrapper >
</template>

<style scoped>

</style>