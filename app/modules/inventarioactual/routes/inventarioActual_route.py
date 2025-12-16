from fastapi import APIRouter, Depends, HTTPException
from app.database.db_connection import get_db
from app.modules.inventarioactual.schemas.inventarioActual_schema import(
    InventarioActualResponse
)
from app.modules.inventarioactual.services.inventarioActual_service import InventarioActualService

router = APIRouter(
    prefix="/inventarioActual",
    tags=["InventarioActual"]
)

@router.get("/", response_model=list[InventarioActualResponse])
def listar_inventarioActual(db=Depends(get_db)):
    service = InventarioActualService(db)
    return service.listar()