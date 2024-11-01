from fastapi import FastAPI

app = FastAPI(title="ChatBot SaaS Platform")

@app.get("/")
async def root():
    return {"message": "Welcome to ChatBot SaaS Platform"}
