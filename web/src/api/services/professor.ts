import api from "../api";
import { ApiResponse } from './types'


/**
 * Fetches the list of professors from the server.
 *
 * @returns {Promise<App.Professor.Professor[]>} A promise that resolves to an array of Professor objects.
 */
export async function getProfessorsInfo(): Promise<ApiResponse<App.Professor.Professor[]>> {
    return api.get<App.Professor.Professor[]>(`professors`);

}

export async function postProfessorInfo(newProfessor: App.Professor.AddProfessor): Promise<ApiResponse<App.Professor.Professor>> {
    return api.post<App.Professor.Professor>('professors', newProfessor);
   
}

export async function addProfessorVote(professorID:string, voteType: 'upvotes' | 'downvotes'): Promise<ApiResponse<App.Professor.Professor>> {
    return api.put(`professors/${voteType}/${professorID}`)
  
}

export async function addProfessorComment(professorID:string, text: string): Promise<ApiResponse<App.Professor.Professor>> {
    return api.put(`professors/comments/${professorID}`, { text })
}

export async function deleteProfessorComment(professorID:string, commentID: string): Promise<ApiResponse<App.Professor.Professor>> {
  
    return api.delete(`professors/comments/${professorID}/${commentID}`)

}




