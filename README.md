<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <a href="https://github.com/joaovitor2614/">
    <img src="web/src/assets/logo_trans.png" width="200" height="200" alt="Logly Logo">
  </a>
</p>

<h1 align="center">Logly</h1>

<p align="center">
  <em>Well log visualization platform (in development ⚙️)</em>
</p>

<p align="center">
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License"></a>
  <a href="https://github.com/joaovitor2614/Mamata-ou-Cilada/stargazers"><img src="https://img.shields.io/github/stars/joaovitor2614/Mamata-ou-Cilada" alt="Stars"></a>
  <a href="https://github.com/joaovitor2614/Mamata-ou-Cilada/network/members"><img src="https://img.shields.io/github/forks/joaovitor2614/Mamata-ou-Cilada" alt="Forks"></a>
  <img src="https://img.shields.io/badge/python-3.10+-blue?logo=python&logoColor=edb641" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-005571?logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Pydantic-005571?logo=pydantic&logoColor=white" alt="Pydantic">
</p>

---

## 🚀 Overview

**Logly** is a platform for **well log visualization**.  
It combines a **Vue.js frontend** with a **FastAPI backend**, enabling efficient data management, user authentication, and interactive visualizations for geoscience workflows.

---

## 🛠️ Main Technologies

- **Frontend:** Vue.js, Vuetify, TypeScript  
- **Backend:** FastAPI, Python  
- **Database:** MongoDB Atlas  
- **Authentication:** Bearer JWT  
- **Testing:** Pytest (backend), Cypress (frontend)  

---

## 📦 Prerequisites

Before running Logly, ensure you have installed:

- [Node.js](https://nodejs.org/) (for frontend development)  
- [Python 3.9+](https://www.python.org/downloads/) (for backend development)  
- [Docker](https://docs.docker.com/get-docker/) & [Docker Compose](https://docs.docker.com/compose/)  
- A [MongoDB Atlas](https://www.mongodb.com/atlas/database) cluster connection string  

---

## ⚙️ Configuration

Create a `.env` file in the **project root** with the following keys:

```env
# MongoDB connection string
MONGO_DB_ATLAS_URI="mongodb+srv://<username>:<password>@cluster0.q5szy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Frontend base URL (local development)
APP_BASE_URL="http://localhost:5173"

# Email credentials for account verification & password reset
VERIFY_ACCOUNT_SENDER_EMAIL_ADDRESS="your-email@gmail.com"
VERIFY_ACCOUNT_SENDER_EMAIL_PASSWORD="your-email-password"