import api from "../api";



/**
 * Fetches the list of professors from the server.
 *
 * @returns {Promise<App.Professor.Professor[]>} A promise that resolves to an array of Professor objects.
 */
export async function getProfessorsInfo(): Promise<App.Professor.Professor[]> {
    const response = await api.get<App.Professor.Professor[]>(`professors`);
    return response.data
}

export async function postProfessorInfo(newProfessor: App.Professor.AddProfessor) {
    await api.post('professors', newProfessor);
}


export async function editProfessorInfo(newProfessor: App.Professor.AddProfessor) {
    await api.put('professors', newProfessor);
}


export async function addProfessorVote(professorID:string, voteType: 'upvotes' | 'downvotes'): Promise<App.Professor.Professor> {
  
    const response = await api.put(`professors/${voteType}/${professorID}`)
    return response.data
}

export async function addProfessorComment(professorID:string, text: string): Promise<App.Professor.Professor> {
  
    const response = await api.put(`professors/comments/${professorID}`, { text })
    return response.data
}


