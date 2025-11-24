from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Calculation API is running"}

