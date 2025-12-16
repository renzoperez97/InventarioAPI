from fastapi import APIRouter, Depends, HTTPException
from app.database.db_connection import get_db
from app.modules.unidadMedida.schemas.unidadMedida_schema import (
    UnidadMedidaCreate, UnidadMedidaUpdate, UnidadMedidaResponse
)
from app.modules.unidadMedida.services.unidadMedida_service import UnidadMedidaService

router = APIRouter(
    prefix="/unidadMedida",
    tags=["unidadMedida"]
)

@router.get("/", response_model=list[UnidadMedidaResponse])
def listar_unidadMedida(db=Depends(get_db)):
    service = UnidadMedidaService(db)
    return service.listar()

@router.get("/{id}", response_model=UnidadMedidaResponse)
def obtener_unidadMedida(id: int, db=Depends(get_db)):
    service = UnidadMedidaService(db)
    unidad = service.obtener(id)
    if not unidad:
        raise HTTPException(status_code=404, detail="Unidad de no encontrado")
    return unidad

@router.post("/")
def crear_unidadMedida(data: UnidadMedidaCreate, db=Depends(get_db)):
    service = UnidadMedidaService(db)
    resultado = service.registrar(data.strNombre, data.strAbreviatura)
    return resultado

@router.put("/")
def actualizar_unidadMedida(data: UnidadMedidaUpdate, db=Depends(get_db)):
    service = UnidadMedidaService(db)
    return service.actualizar(
        data.intUnidadMedidaID,
        data.strNombre,
        data.strAbreviatura
    )

@router.put("/anular/{id}")
def anular_unidadMedida(id: int, db=Depends(get_db)):
    service = UnidadMedidaService(db)
    return service.anular(id)