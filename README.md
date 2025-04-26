<!-- markdownlint-disable MD033 MD041 -->

<p align="center">
  <a href="https://github.com/joaovitor2614/"><img src="web/public/logo.svg" width="200" height="200" alt="github"></a>
</p>

<div align="center">

# Mamata ou Cilada
<!-- prettier-ignore-start -->
<!-- markdownlint-disable-next-line MD036 -->

[![license](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![github stars](https://img.shields.io/github/stars/joaovitor2614/Mamata-ou-Cilada)](https://github.com/joaovitor2614/Mamata-ou-Cilada)
[![github forks](https://img.shields.io/github/forks/joaovitor2614/Mamata-ou-Cilada)](https://github.com/joaovitor2614/Mamata-ou-Cilada)
![python](https://img.shields.io/badge/python-3.10+-blue?logo=python&logoColor=edb641)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=python&logoColor=edb641)

![Pydantic](https://img.shields.io/badge/Pydantic-005571?logo=pydantic&logoColor=edb641)

# Summary
Mamata ou Cilada is a web app focused for student users to help them evaluate and feedback professors


## Main Technologies
- **Frontend:** Vue.js, Vuetify, TypeScript
- **Backend:** FastAPI, Python, MongoDB
- **Testing:** Pytest, Cypress
- **Authentication**: Bearer JWT

### Prerequisites
- Node.js (for frontend development)
- Python 3.9+ (for backend development)
- MongoDB Atlas Cluster connection string

## How to run it
Step 1 - Clone Repo
   ```
   cd kinit-api
   
   pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
   ```

Step 2 - Install front-end dependencies
   ```
   cd web
   
   npm install
   ```

Step 3 - Install back-end dependencies
   ```
   cd ..

   cd app
   
   pip install -r requirements.txt 
   ```

Step 4 - Create .env file at app/settings and add mongo db connection string

  ```
   MONGO_DB_ATLAS_URI="mongodb+srv://<user_name>:<user_db_password></user_db_password>@cluster0.q5szy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
   ```
Step 5 - Run the app:
   ```
   cd ..
   cd web
   npm run dev-on
   ```


</div>