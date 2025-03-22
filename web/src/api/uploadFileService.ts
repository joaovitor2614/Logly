import api from './api'

import http from "../http-common";

class UploadFilesService {
  upload(file, onUploadProgress) {
    let formData = new FormData();

    formData.append("file", file);

    return api.post("professors/upload", formData, {
      headers: {
        "Content-Type": "multipart/form-data"
      },
     
    });
  }

  getFiles() {
    return api.get("/files");
  }
}

export default new UploadFilesService();