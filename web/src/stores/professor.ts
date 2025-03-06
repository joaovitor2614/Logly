import { defineStore } from "pinia"
import { reactive, Ref, ref } from "vue"
import { useToast } from "vue-toastification";
import api from '../api/api'



export const useProfessorStore = defineStore('professorStore', () => {
    const professorCollection: Ref<App.Professor[]> = ref([])
    const toast = useToast();

    function getProfessorCollection() {
        return professorCollection.value
    }

    async function fetchProfessorsInfo() {
        try {
            const response = await api.get(`professors`)
            console.log('response', response.data)
            professorCollection.value = response.data

        } catch (error) {
            toast.error(error.response.data.detail);
        }
    
    }

    

    return {
        getProfessorCollection,
        fetchProfessorsInfo
    }
    
})