from fastapi import FastAPI

app = FastAPI()

#PASS APERATION OR ROUTER
@app.get("/")
async def login_user():
    context = {'message' : 'hellow world'}
    return context