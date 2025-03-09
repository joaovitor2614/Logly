import { defineStore } from "pinia"
import { reactive, Ref, ref } from "vue"
import { useToast } from "vue-toastification";
import api from '../api/api'

interface ProfessorFilters {
    name: string
}



export const useProfessorStore = defineStore('professorStore', () => {
    const professorCollection: Ref<App.Professor[]> = ref([])
    const toast = useToast();
    const filters: ProfessorFilters = {
        name: ''
    }

    function getProfessorCollection() {
        return professorCollection.value.filter((professor) => {
            const nameMatch = professor.name.toLowerCase().includes(filters.name.toLocaleLowerCase())

            return nameMatch
        })
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
        fetchProfessorsInfo,
        professorCollection,
        filters
    }
    
})