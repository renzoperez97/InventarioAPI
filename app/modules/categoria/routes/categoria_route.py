from fastapi import APIRouter, Depends, HTTPException
from app.database.db_connection import get_db
from app.modules.categoria.schemas.categoria_schema import (
    CategoriaCreate,CategoriaUpdate, CategoriaResponse
)
from app.modules.categoria.services.categoria_service import CategoriaService

router = APIRouter(
    prefix="/categoria",
    tags=["categoria"]
)

@router.get("/", response_model=list[CategoriaResponse])
def listar_categoria(db=Depends(get_db)):
    service = CategoriaService(db)
    return service.listar()

@router.get("/{id}", response_model=CategoriaResponse)
def obtener_categoria(id: int, db=Depends(get_db)):
    service = CategoriaService(db)
    unidad = service.obtener(id)
    if not unidad:
        raise HTTPException(status_code=404, detail="Unidad de no encontrado")
    return unidad

@router.post("/")
def crear_categoria(data: CategoriaCreate, db=Depends(get_db)):
    service = CategoriaService(db)
    resultado = service.registrar(data.strNombre, data.strDescripcion)
    return resultado

@router.put("/")
def actualizar_categoria(data: CategoriaUpdate, db=Depends(get_db)):
    service = CategoriaService(db)
    return service.actualizar(
        data.intCategoriaID,
        data.strNombre,
        data.strDescripcion
    )

@router.put("/anular/{id}")
def anular_categoria(id: int, db=Depends(get_db)):
    service = CategoriaService(db)
    return service.anular(id)