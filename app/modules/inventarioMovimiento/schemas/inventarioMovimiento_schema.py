from pydantic import BaseModel
from datetime import datetime

class InventarioMovimientoBase(BaseModel):
    intProductoID: int
    intAlmacenID: int
    strTipoMovimiento: str
    decCantidad: float
    decCostoUnitario: float
    strDocumentoRef: str
    strObservacion: str

class InventarioMovimientoCreate(InventarioMovimientoBase):
    pass

class InventarioMovimientoUpdate(InventarioMovimientoBase):
    pass

class InventarioMovimientoResponse(BaseModel):
    intMovimientoID: int
    intProductoID: int
    strProducto: str
    intAlmacenID: int
    strAlmacen: str
    intUsuarioID: int
    strUsuario: str
    strFechaMovimiento: str
    strTipoMovimiento: str
    decCantidad: float
    decCostoUnitario: float
    strDocumentoRef: str
    strObservacion: str


