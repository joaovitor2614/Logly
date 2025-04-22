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
      
            const { professorsInfo, hasErrors } = await getProfessorsInfo()
            if (!hasErrors) {
                professorCollection.value = professorsInfo
            }   
            
    }

    async function addProfessor(newProfessorData: App.Professor.AddProfessor) {
        const { professorInfo, hasErrors } = await postProfessorInfo(newProfessorData)
        if (!hasErrors) {
            toast.success(`${newProfessorData.name} added successfully!`);
            await fetchProfessorsInfo()
        }

    
    }
    
    async function rankProssessor(professorID:string, voteType: 'upvotes' | 'downvotes') {
       
      
        const { professorInfo, hasErrors } = await addProfessorVote(professorID, voteType)
            
            
        professorCollection.value.forEach((professor) => {
            if (professor._id == professorID) {
                professor[`${voteType}`] = professorInfo[`${voteType}`]
            }
        })
  
 
       
    }

    async function commentProfessor(professorID:string, text: string) {
       

        const  { professorInfo, hasErrors } = await addProfessorComment(professorID, text)

        professorCollection.value.forEach((professor) => {
            if (professor._id == professorID) {
                professor["comments"] = professorInfo["comments"]
            }
        })

         
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