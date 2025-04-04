import { defineStore } from "pinia"
import { Ref, ref, computed } from "vue"
import { useToast } from "vue-toastification";
import { fetchProfessorsInfo, addProfessorRequest } from '@/api/services/professor'
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
      
            const response = await api.get<App.Professor.Professor[]>(`professors`);
            professorCollection.value = response.data

       
    
    }



    async function addProfessor(newProfessorData: App.Professor.AddProfessor) {
        try {
      
            await addProfessorRequest(newProfessorData)
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

    async function commentProfessor(professorID: App.Professor._id, text: string) {
       
        try {
             const response = await api.put(`professors/comments/${professorID}`, {"text": text})
             const newProfessorData = response.data
         
           
             professorCollection.value.forEach((professor) => {
                 if (professor._id == professorID) {
                     professor["comments"] = newProfessorData["comments"]
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
        commentProfessor,
        addProfessor,
        filters
    }
    
})