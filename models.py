from pydantic import BaseModel
from typing import Optional

class Persona(BaseModel):
    nombre: str
    edad: int
    ciudad: str
    email: str
    telefono: str
    ocupacion: str
