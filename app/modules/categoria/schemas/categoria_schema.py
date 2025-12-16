from pydantic import BaseModel

class CategoriaBase(BaseModel):
    strNombre: str
    strDescripcion: str

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(CategoriaBase):
    intCategoriaID: int

class CategoriaResponse(BaseModel):
    intCategoriaID: int
    strNombre: str
    strDescripcion: str