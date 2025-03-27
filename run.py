import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", port=5000, log_level="info", reload=True, timeout_graceful_shutdown=10000, timeout_keep_alive=10000)