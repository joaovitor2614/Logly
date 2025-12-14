import { getWellLogDataByIDs, getRefDepthWellLogData } from "@/api/services/well"

const convertStringfiedArrayToArray = (stringfiedData: string) => {
    return stringfiedData
    .split(",")                
    .map(s => s.trim())       
    .map(s => s === "NaN" ? NaN : parseFloat(s)); 
    
}   

export const getWellLogDataByID = async (wellLogID: string, wellID: string) => {
    const response = await getWellLogDataByIDs(wellLogID, wellID)
    if (response) {
        const wellLogData = convertStringfiedArrayToArray(response.data.data)
        return wellLogData
    } else {
        return []
    }
        
    
}

export const getDepthWellLogData = async (wellID: string) => {
    const response = await getRefDepthWellLogData(wellID)
    if (response) {
        const wellLogData = convertStringfiedArrayToArray(response.data.data)
        return wellLogData
    } else {
        return []
    }
        
    
}