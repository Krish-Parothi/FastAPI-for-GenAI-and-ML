from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
    return {"message":"Hello"}


@app.get("/about")
async def about():
    return {'message':'Krish Parothi is the 2nd Year Student in Ramdeobaba University'}