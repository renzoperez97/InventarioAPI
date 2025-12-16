from pydantic import BaseModel

class ProductoBase(BaseModel):
    intUnidadMedidaID: int
    intCategoriaID: int
    strProducto: str    
    decPrecio: float
    decCosto: float

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    intProductoID: int

class ProductoResponse(BaseModel):
    intProductoID: int
    strUnidadMedida: str
    strCategoria: str
    strProducto: str    
    decPrecio: float
    decCosto: float
    strFechaCreacion: str


