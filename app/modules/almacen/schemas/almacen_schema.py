from pydantic import BaseModel

class AlmacenBase(BaseModel):
    strNombre: str
    strDireccion: str

class AlmacenCreate(AlmacenBase):
    pass

class AlmacenUpdate(AlmacenBase):
    intAlmacenID: int

class AlmacenResponse(BaseModel):
    intAlmacenID: int
    strNombre: str
    strDireccion: str
