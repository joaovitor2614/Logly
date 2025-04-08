import { defineStore } from "pinia"
import { Ref, ref, computed } from "vue"
import { useToast } from "vue-toastification";
import { fetchProfessorsInfo, addProfessorRequest } from '@/api/services/professor'
import { ProfessorFilters } from './types'
import api from '../../api/api'
import getFilteredProfessorCollection from './filter'




export const useProfessorStore = defineStore('professorStore', () => {
    const professorCollection: Ref<App.Professor.Professor[]> = ref([])
    const shouldOpenAddProfessorDialog = ref(false)
    const toast = useToast();
    const filters: Ref<ProfessorFilters> = ref({
        name: '',
        gender: '',
        sortBy: '',
    })

    const finalProfessorCollection = computed(() => {
        
        const professorFilteredCollection = getFilteredProfessorCollection(professorCollection.value, filters.value)
        const professorSortedCollection = filters.value.sortBy 
        ? professorFilteredCollection.sort((a, b) => b[filters.value.sortBy].length - a[filters.value.sortBy].length) 
        : professorFilteredCollection
        return professorSortedCollection
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
        finalProfessorCollection,
        fetchProfessorsInfo,
        shouldOpenAddProfessorDialog,
        rankProssessor,
        professorCollection,
        commentProfessor,
        addProfessor,
        filters
    }
    
})