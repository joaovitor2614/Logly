import { defineStore } from "pinia"
import { Ref, ref, computed } from "vue"
import { useToast } from "vue-toastification";
import { 
    getAvaiablesProfessorDisciplines, 
    getProfessorsInfo, 
    postProfessorInfo, 
    addProfessorVote,
    addProfessorComment, 
    deleteProfessorComment 
} from '@/api/services/professor'
import { ProfessorFilters } from './types'
import getFilteredProfessorCollection from './filter'




export const useProfessorStore = defineStore('professorStore', () => {
    const professorCollection: Ref<App.Professor.Professor[]> = ref([])
    const availableProfessorDisciplines: Ref<string[]> = ref([])
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
      
            const { data: professorsInfo, hasErrors } = await getProfessorsInfo()
            if (!hasErrors) {
                professorCollection.value = professorsInfo
            }   
            
    }

    async function fetchAvailableProfessorDisciplines() {
        const { data: disciplines, hasErrors } = await getAvaiablesProfessorDisciplines()
        if (!hasErrors) {
            availableProfessorDisciplines.value = disciplines
        }
    }

    const updateProfessorField = (professorID: string, fieldKey: keyof App.Professor.Professor, newFieldValue: any[]) => {
        professorCollection.value.forEach((professor) => {
            if (professor._id == professorID) {
                professor[fieldKey] = newFieldValue
            }
        })
    }

    async function addProfessor(newProfessorData: App.Professor.AddProfessor) {
        const { data: professorInfo, hasErrors } = await postProfessorInfo(newProfessorData)
        if (!hasErrors) {
            professorCollection.value.push(professorInfo)
            toast.success(`${newProfessorData.name} added successfully!`);
        }
        return hasErrors

    
    }
    
    async function rankProssessor(professorID:string, voteType: 'upvotes' | 'downvotes') {
       
      
        const { data: professorInfo, hasErrors } = await addProfessorVote(professorID, voteType)
        if (!hasErrors) {
            updateProfessorField(professorID, voteType, professorInfo[`${voteType}`])
        }
            
        updateProfessorField(professorID, voteType, professorInfo[`${voteType}`])
       
    }

    async function commentProfessor(professorID:string, text: string) {
       

        const  { data: professorInfo, hasErrors } = await addProfessorComment(professorID, text)
        if (!hasErrors) {
            updateProfessorField(professorID, "comments", professorInfo["comments"])  
        }
     }

     async function deleteComment(professorID:string, commentID: string) {
       

        const  { data: professorInfo, hasErrors } = await deleteProfessorComment(professorID, commentID)
        if (!hasErrors) {
            updateProfessorField(professorID, "comments", professorInfo["comments"])  
        }
     }


    return {
        finalProfessorCollection,
        fetchProfessorsInfo,
        fetchAvailableProfessorDisciplines,
        availableProfessorDisciplines,
        shouldOpenAddProfessorDialog,
        rankProssessor,
        professorCollection,
        commentProfessor,
        deleteComment,
        addProfessor,
        filters
    }

})