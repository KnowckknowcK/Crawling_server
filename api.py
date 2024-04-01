from fastapi import FastAPI

app = FastAPI()

@app.get("/",)
async def post_articles():
    return {"message":"hello"}