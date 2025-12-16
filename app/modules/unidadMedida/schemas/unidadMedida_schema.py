from pydantic import BaseModel

class UnidadMedidaBase(BaseModel):
    strNombre: str
    strAbreviatura: str

class UnidadMedidaCreate(UnidadMedidaBase):
    pass

class UnidadMedidaUpdate(UnidadMedidaBase):
    intUnidadMedidaID: int

class UnidadMedidaResponse(BaseModel):
    intUnidadMedidaID: int
    strNombre: str
    strAbreviatura: str