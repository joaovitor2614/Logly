import api from "../api";


export async function importWellFile(lasFilePath: string, wellName: string) {
    await api.post(`/well`, { file_path: lasFilePath, well_name: wellName });
}