import { ProfessorFilters } from './types'


const getFilteredProfessorCollection = (professors: App.Professor.Professor[], filters: ProfessorFilters) => {
    return professors.filter((professor) => {
        const professorNameMatch = professor.name.toLowerCase().includes(filters.name.toLocaleLowerCase())
        let professorGenderMatch = filters.gender ? professor.gender == filters.gender : true
     
        return professorNameMatch && professorGenderMatch

      
    })
}

export default getFilteredProfessorCollection