---- api.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/fvasquez")
async def root():
    return {
        "name": "Francisco",
        "email": "frvasquezjaquez@gmail.com",
        "clase": "DevOps" 
     }    
     
     
--- Requirements

fastapi
uvicorn


--- README.md

# Ejecucion

1. Instalamos las dependencias
```
pip install -r requirements.txt
```

2. Iniciamos la aplicacion
```
uvicorn api:app
```