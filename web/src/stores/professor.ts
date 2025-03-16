import { defineStore } from "pinia"
import { reactive, Ref, ref, computed } from "vue"
import { useToast } from "vue-toastification";
import api from '../api/api'

interface ProfessorFilters {
    name: string
}



export const useProfessorStore = defineStore('professorStore', () => {
    const professorCollection: Ref<App.Professor[]> = ref([])
    const toast = useToast();
    const filters: Ref<ProfessorFilters> = ref({
        name: ''
    })

    const professorFilteredCollection = computed(() => {
        console.log('professorFilteredCollection re computed')
        return professorCollection.value.filter((professor) => {
            const nameMatch = professor.name.toLowerCase().includes(filters.value.name.toLocaleLowerCase())

            return nameMatch
        })

    })

    async function fetchProfessorsInfo() {
        try {
            const response = await api.get(`professors`)
            console.log('response', response.data)
            professorCollection.value = response.data

        } catch (error) {
            toast.error(error.response.data.detail);
        }
    
    }

    async function editProfessor(professorID: string, newProfessorData: App.Professor) {
        try {
            delete newProfessorData._id
            const {data: updatedProfessorData} = await api.put<App.Professor>(`professors/${professorID}`, newProfessorData)
            console.log('updatedProfessorData', updatedProfessorData)
       
            const index = professorCollection.value.findIndex((professor) => professor._id == professorID)
            if (index !== -1) {
                console.log('here')
                professorCollection.value[index] = {...updatedProfessorData}
                console.log('professorCollection.value[index]', professorCollection.value[index])
            }
            console.log('professorCollection.value', professorCollection.value)

        } catch (error) {
            toast.error(error.response.data.detail);
        }
    
    }

    

    return {
        professorFilteredCollection,
        fetchProfessorsInfo,
        professorCollection,
        editProfessor,
        filters
    }
    
})