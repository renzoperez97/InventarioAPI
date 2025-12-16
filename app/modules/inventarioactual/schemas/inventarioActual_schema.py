from pydantic import BaseModel

class InventarioActualBase(BaseModel):
    intInventarioID: int
    intProductoID: int
    intAlmacenID: int
    decStock: float
    decStockMinimo: float
    decStockMaximo: float
    decStockReservado: float

class InventarioActualCreate(InventarioActualBase):
    pass

class InventarioActualUpdate(InventarioActualBase):
    pass

class InventarioActualResponse(BaseModel):
   intInventarioID: int
   strProducto: str
   strAlmacen: str
   decStock: float
   decStockReservado: float

