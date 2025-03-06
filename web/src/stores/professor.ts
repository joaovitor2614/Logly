import { defineStore } from "pinia"
import { reactive, Ref, ref } from "vue"

import api from '../api/api'



export const useProfessorStore = defineStore('professorStore', () => {
    const professorCollection: Ref<App.Professor[]> = ref([])


    function getProfessorCollection() {
        return professorCollection.value
    }

    

    return {
        getProfessorCollection
    }
    
})