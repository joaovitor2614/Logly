<script setup lang="ts">
import { reactive } from 'vue';
import useVuelidate from '@vuelidate/core';
import { required} from '@vuelidate/validators'
import { computed } from 'vue';
import Button from '@/components/common/Button.vue'
import { importWellFile } from '@/api/services/well'


const form = reactive({
    lasFilePath: '',
    wellName: ''
})

const rules = {
    lasFilePath: { required, $autoDirty: true },
    wellName: { required, $autoDirty: true }
}
const v$ = useVuelidate(rules, form);
const isDisabled = computed(() => v$.value.lasFilePath.$invalid || v$.value.wellName.$invalid ? true : false);

const importWell = () => {
    importWellFile(form.lasFilePath, form.wellName)
}
</script>

<template>
    <v-card>
        <v-card-title class="grey lighten-2">Import</v-card-title>
        <v-card-text>
            <v-row>
                <v-col cols="6">
                    <v-text-field 
                    type="text" 
                    label="LAS File" 
                    v-model="form.lasFilePath"
                    append-inner-icon="mdi-folder-open" 
                    />
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="6">
                    <v-text-field 
                    type="text" 
                    v-model="form.wellName"
                    label="Well name" 
           
         
                    />
                </v-col>
            </v-row>
            <Button 
            :id="'test-import-well-btn'"
            :buttonAction="importWell"
            :is-disabled="isDisabled"
            
            >
                Import
            </Button>        
        </v-card-text>
    </v-card>
</template>

<style scoped>

</style>