from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Podcast AI Backend is live!"}

@app.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    return {"filename": file.filename}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
