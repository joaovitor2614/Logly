import { defineStore } from "pinia"
import { Ref, ref, computed } from "vue"
import { useToast } from "vue-toastification";
import api from '../api/api'

interface ProfessorFilters {
    name: string,
    gender: 'all' | 'male' | 'female'
}



export const useProfessorStore = defineStore('professorStore', () => {
    const professorCollection: Ref<App.Professor.Professor[]> = ref([])
    const shouldOpenAddProfessorDialog = ref(false)
    const toast = useToast();
    const filters: Ref<ProfessorFilters> = ref({
        name: '',
        gender: 'all'
    })


    const professorFilteredCollection = computed(() => {
        console.log('professorFilteredCollection re computed')
        return professorCollection.value.filter((professor) => {
            const professorNameMatch = professor.name.toLowerCase().includes(filters.value.name.toLocaleLowerCase())
            let professorGenderMatch = true;
            if (filters.value.gender !== 'all') {
                professorGenderMatch = professor.gender == filters.value.gender
            } 
            return professorNameMatch && professorGenderMatch

          
        })

    })

    async function fetchProfessorsInfo() {
        try {
            const response = await api.get<App.Professor.Professor[]>(`professors`)
            console.log('response', response.data)
            professorCollection.value = response.data

        } catch (error) {
            toast.error(error.response.data.detail);
        }
    
    }



    async function addProfessor(newProfessorData: App.Professor.AddProfessor) {
        try {
      
            await api.post(`professors`, newProfessorData)
            toast.success(`${newProfessorData.name} added successfully!`);
            await fetchProfessorsInfo()

          
       


        } catch (error) {
            toast.error(error.response.data.detail);
        }
    
    }

    async function rankProssessor(professorID: App.Professor._id, voteType: 'upvotes' | 'downvotes') {
       
       try {
            const response = await api.put(`professors/${voteType}/${professorID}`)
            const newProfessorData = response.data
          
            professorCollection.value.forEach((professor) => {
                if (professor._id == professorID) {
                    professor[`${voteType}`] = newProfessorData[`${voteType}`]
                }
            })
  
 
        } catch (error) {
            toast.error(error.response.data.detail);
        }
    }

    

    return {
        professorFilteredCollection,
        fetchProfessorsInfo,
        shouldOpenAddProfessorDialog,
        rankProssessor,
        professorCollection,
        addProfessor,
        filters
    }
    
})