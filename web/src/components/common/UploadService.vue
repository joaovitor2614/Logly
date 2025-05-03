<script setup lang="ts">
import fallBackImage from '@/assets/fallBackProfileImage.jpg'
import { onMounted } from 'vue'
import UploadFilesService from '../../api/uploadFileService'
import { ref, onBeforeMount } from 'vue'

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

onBeforeMount(() => {
    if (!image.value) {
        previewImage.value = fallBackImage
        console.log('previewImage.value', previewImage.value)
    }
})
</script>

<template>
 
        <v-row class="d-flex align-center justify-center">
            <v-col cols="12" class="mt-4 mb-4">
                <label 
                    for="image-input" 
                    class="avatar-wrapper d-flex justify-center align-center img-avatar" 
                    style="width: 150px; height: 150px; border-radius: 50%; cursor: pointer"
                >
                    <input type="file" id="image-input" class="avatar-image" @change="selectImage" style="display: none" />
                    <v-img alt="Preview Image" :src="previewImage"></v-img>
                    <div class="avatar-overlay">Change your avatar</div>
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

.avatar-wrapper {
  position: relative;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  overflow: hidden;
  cursor: pointer;
  display: inline-block;
}

.avatar-image {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
}

.avatar-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background-color: rgba(0, 0, 0, 0.6);
  color: white;
  font-size: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
  text-align: center;
}

.avatar-wrapper:hover .avatar-overlay {
  opacity: 0.8;
}
</style>