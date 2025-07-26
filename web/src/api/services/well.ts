import api from "../api";


export async function importWellFile(lasFilePath: string, wellName: string) {
    return await api.post(`/well`, { file_path: lasFilePath, well_name: wellName });
}


export async function getAllWellsData() {
    return await api.get<App.Well.Well[]>(`/well`);
}

export async function deleteWellByID(wellID: string) {
    return await api.delete(`/well/${wellID}`);
}

