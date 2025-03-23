import api from './api'

import http from "../http-common";

class UploadFilesService {
  async upload(file, onUploadProgress) {
    let formData = new FormData();

    formData.append("file", file);

    const response = await api.post("professors/upload", formData, {
      headers: {
        "Content-Type": "multipart/form-data"
      },
     
    });
    return response.data.imageUrl
  }

  getFiles() {
    return api.get("/files");
  }
}

export default new UploadFilesService();