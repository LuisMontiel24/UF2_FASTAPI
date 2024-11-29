from fastapi import FastAPI, HTTPException
from models import Persona
from database import personas_db

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API Roger Sobrino Gil"}

# Endpoint GET para obtener una persona por su ID
@app.get("/personas/{persona_id}")
def get_persona(persona_id: int):
    if persona_id not in personas_db:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return personas_db[persona_id]

# Endpoint POST para crear una nueva persona
@app.post("/personas/")
def create_persona(persona: Persona):
    persona_id = len(personas_db) + 1
    # Agrega diccionario personas_db
    personas_db[persona_id] = persona.dict()
    return {"persona_id": persona_id, "data": persona}
