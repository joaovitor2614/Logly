<!-- markdownlint-disable MD033 MD041 -->

<p align="center">
  <a href="https://github.com/joaovitor2614/"><img src="web/public/logo.svg" width="200" height="200" alt="github"></a>
</p>

<div align="center">

# Logly
<!-- prettier-ignore-start -->
<!-- markdownlint-disable-next-line MD036 -->


</div>
# Summary



## Main Technologies
- **Frontend:** Vue.js, Vuetify, TypeScript
- **Backend:** FastAPI, Python,
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


