from fastapi import APIRouter, Depends, HTTPException
from app.database.db_connection import get_db
from app.modules.almacen.schemas.almacen_schema import (
    AlmacenCreate, AlmacenUpdate, AlmacenResponse
)
from app.modules.almacen.services.almacen_service import AlmacenService

router = APIRouter(
    prefix="/almacenes",
    tags=["Almacenes"]
)

@router.get("/", response_model=list[AlmacenResponse])
def listar_almacenes(db=Depends(get_db)):
    service = AlmacenService(db)
    return service.listar()

@router.get("/{id}", response_model=AlmacenResponse)
def obtener_almacen(id: int, db=Depends(get_db)):
    service = AlmacenService(db)
    almacen = service.obtener(id)
    if not almacen:
        raise HTTPException(status_code=404, detail="Almacén no encontrado")
    return almacen

@router.post("/")
def crear_almacen(data: AlmacenCreate, db=Depends(get_db)):
    service = AlmacenService(db)
    resultado = service.registrar(data.strNombre, data.strDireccion)
    return resultado

@router.put("/")
def actualizar_almacen(data: AlmacenUpdate, db=Depends(get_db)):
    service = AlmacenService(db)
    return service.actualizar(
        data.intAlmacenID,
        data.strNombre,
        data.strDireccion
    )

@router.put("/anular/{id}")
def anular_almacen(id: int, db=Depends(get_db)):
    service = AlmacenService(db)
    return service.anular(id)