from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/upload")
async def upload_resume():
    return {"message": "Upload endpoint"}

@app.get("/submit")
async def submit_resume():
    return {"message": "Submit endpoint"}