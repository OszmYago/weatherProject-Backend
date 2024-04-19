from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def login():
    return {"Hello world"}

@app.get("/user")
def userExperience()
    return {"Experiencia de Usuário:"}