import api from "../api";



/**
 * Fetches the list of professors from the server.
 *
 * @returns {Promise<App.Professor.Professor[]>} A promise that resolves to an array of Professor objects.
 */
export async function getProfessorsInfo(): Promise<{ professorsInfo: App.Professor.Professor[], hasErrors: boolean }> {
    const { data, hasErrors } = await api.get<App.Professor.Professor[]>(`professors`);
    return { professorsInfo: data, hasErrors}
}

export async function postProfessorInfo(newProfessor: App.Professor.AddProfessor): Promise<{ professorInfo: App.Professor.Professor, hasErrors: boolean }> {
    const { data, hasErrors } = await api.post<App.Professor.Professor>('professors', newProfessor);
    return { professorInfo: data, hasErrors}
}


export async function editProfessorInfo(newProfessor: App.Professor.AddProfessor): Promise<{ professorInfo: App.Professor.Professor, hasErrors: boolean }> {
    const { data, hasErrors }  = await api.put('professors', newProfessor);
    return { professorInfo: data, hasErrors}
}


export async function addProfessorVote(professorID:string, voteType: 'upvotes' | 'downvotes'): Promise<{ professorInfo: App.Professor.Professor, hasErrors: boolean }> {
  
    const { data, hasErrors } = await api.put(`professors/${voteType}/${professorID}`)
    return{ professorInfo: data, hasErrors}
}

export async function addProfessorComment(professorID:string, text: string): Promise<{ professorInfo: App.Professor.Professor, hasErrors: boolean }> {
  
    const { data, hasErrors } = await api.put(`professors/comments/${professorID}`, { text })
    return{ professorInfo: data, hasErrors}
}

export async function deleteProfessorComment(professorID:string, commentID: string): Promise<{ professorInfo: App.Professor.Professor, hasErrors: boolean }> {
  
    const { data, hasErrors } = await api.delete(`professors/comments/${professorID}/${commentID}`)
    return{ professorInfo: data, hasErrors}
}



