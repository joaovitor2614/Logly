<script setup lang="ts">
import {UploadFilesService} from '../../api/uploadFileService'
import { ref } from 'vue'
const currentImage = ref('')
const previewImage = ref('')

const progress = ref(0)
const message = ref('')
const imageInfos = ref([])

const selectImage = (event: Event) =>{
    const input = event.target as HTMLInputElement;
    if (input.files && input.files[0]) {
        currentImage.value = input.files[0];
        previewImage.value = URL.createObjectURL(currentImage.value); // Create preview URL
        progress.value = 0;
        message.value = "";
    }
}
</script>

<template>
    <v-row no-gutters  align="center" justify="center">
        <v-col cols="8">
            <v-file-input
                show-size
                label="Select Image"
                accept="image/*"
                @change="selectImage"
            ></v-file-input>
        </v-col>
        <v-col cols="4" v-if="previewImage">

            <v-avatar size="150">
                <v-img
                    alt="Preview Image"
                    :src="previewImage"
                ></v-img>
            </v-avatar>
                             
        </v-col>
    </v-row>
</template>

<style scoped>

</style>