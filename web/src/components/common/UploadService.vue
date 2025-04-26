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

    const imageUrl = await UploadFilesService.upload(currentImage.value)

    image.value = imageUrl
}

</script>

<template>
 
        <v-row class="d-flex align-center justify-center">
            <v-col cols="12" class="mt-4 mb-4">
                <label for="image-input" class="d-flex justify-center align-center img-avatar" style="width: 150px; height: 150px; border-radius: 50%; cursor: pointer">
                    <input type="file" id="image-input" @change="selectImage" style="display: none" />
                    <v-img alt="Preview Image" :src="image"></v-img>
                </label>
               
            </v-col>
        </v-row>

        
                             
    
   
</template>

<style scoped>
#image-input {
  border-radius: 50%;
}
label[for="image-input"] {
  border-radius: 50%;
}
</style>