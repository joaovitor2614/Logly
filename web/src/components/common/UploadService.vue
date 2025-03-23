<script setup lang="ts">
import UploadFilesService from '../../api/uploadFileService'
import { ref } from 'vue'
const currentImage = ref('')
const previewImage = ref('')


const image = defineModel('image', { required: true, type: String })



const selectImage = (event: Event) =>{
    const input = event.target as HTMLInputElement;
    if (input.files && input.files[0]) {
        currentImage.value = input.files[0];
        previewImage.value = URL.createObjectURL(currentImage.value); 
        upload()

    }
}
const upload = async () => {
    if (!currentImage.value) {
        return
    }
    console.log('here current image', currentImage.value)
    const imageUrl = await UploadFilesService.upload(currentImage.value)
    console.log('imageUrl', imageUrl)
    image.value = imageUrl
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