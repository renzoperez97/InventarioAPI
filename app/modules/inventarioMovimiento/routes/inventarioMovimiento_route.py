from fastapi import APIRouter, Depends, HTTPException, Query
from app.database.db_connection import get_db
from app.modules.inventarioMovimiento.schemas.inventarioMovimiento_schema import(
    InventarioMovimientoCreate, InventarioMovimientoResponse
)
from app.modules.inventarioMovimiento.services.inventarioMovimiento_service import InventarioMovimientoService

router = APIRouter(
    prefix="/inventarioMovimiento",
    tags=["InventarioMovimiento"]
)

@router.get("/obtener", response_model=list[InventarioMovimientoResponse])
def listar_movimiento(
    productoID: int = Query(None, description="ID del producto"),
    almacenID: int = Query(None, description="ID del almacén"),
    db=Depends(get_db)
):
    service = InventarioMovimientoService(db)
    movimientos = service.listar_movimientos(productoID, almacenID)

    if not movimientos:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")

    return movimientos  # Devuelve toda la lista

@router.post("/")
def crear_movimiento(data: InventarioMovimientoCreate, db=Depends(get_db)):
    service = InventarioMovimientoService(db)
    resultado = service.registrar(
        data.intProductoID,
        data.intAlmacenID,
        data.strTipoMovimiento,
        data.decCantidad,
        data.decCostoUnitario,
        data.strDocumentoRef,
        data.strObservacion
    )
    return resultado
