import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", port=5000, host="0.0.0.0", log_level="info")