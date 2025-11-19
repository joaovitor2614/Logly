import api from "../api";


export async function importWellFile(lasFile: File) {

    const formData = new FormData();
    formData.append("las_file", lasFile); 

    return await api.post(`/well`, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    }});
}




export async function getWellBasicInfoFromFile(lasFile: File) {

    const formData = new FormData();
    formData.append("las_file", lasFile); 

    return await api.post(`/well/pre-import-info`, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    }});
}


export async function getAllWellsData() {
    return await api.get<App.Well.Well[]>(`/well`);
}

interface GetWellLogResponse {
    data: string
}

export async function  getRefDepthWellLogData(wellID: string)  {
    return await api.get<GetWellLogResponse>(`/well/data/ref_depth_data/${wellID}`);
}
export async function getWellLogDataByIDs(wellLogID: string, wellID: string) {
    return await api.get<GetWellLogResponse>(`/well/data/${wellID}/${wellLogID}`);
}


export async function deleteWellByID(wellID: string) {
    return await api.delete(`/well/${wellID}`);
}


export async function deleteWellLogByIDS(wellLogID: string,wellID: string) {
    return await api.delete(`/well/data/${wellID}/${wellLogID}`);
}
