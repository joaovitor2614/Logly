import { defineStore } from "pinia"
import { Ref, ref, computed } from "vue"
import { useToast } from "vue-toastification";
import { getProfessorsInfo, postProfessorInfo, addProfessorVote, addProfessorComment } from '@/api/services/professor'
import { ProfessorFilters } from './types'
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
      
            const professorInfo = await getProfessorsInfo()
            professorCollection.value = professorInfo

    }


    async function addProfessor(newProfessorData: App.Professor.AddProfessor) {
        try {
      
            await postProfessorInfo(newProfessorData)
            toast.success(`${newProfessorData.name} added successfully!`);
            await fetchProfessorsInfo()


        } catch (error) {
            toast.error(error.response.data.detail);
        }
    
    }
    
    async function rankProssessor(professorID:string, voteType: 'upvotes' | 'downvotes') {
       
       try {
            const newProfessorData = await addProfessorVote(professorID, voteType)
          
          
            professorCollection.value.forEach((professor) => {
                if (professor._id == professorID) {
                    professor[`${voteType}`] = newProfessorData[`${voteType}`]
                }
            })
  
 
        } catch (error) {
            toast.error(error.response.data.detail);
        }
    }

    async function commentProfessor(professorID:string, text: string) {
       
        try {
             const newProfessorData = await addProfessorComment(professorID, text)

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