import api from "../api";



export async function fetchProfessorsInfo(): Promise<App.Professor.Professor[]> {
    const response = await api.get<App.Professor.Professor[]>(`professors`);
    return response.data
}

export async function addProfessorRequest(newProfessor: App.Professor.AddProfessor) {
    await api.post('professors', newProfessor);
}