from fastapi import APIRouter, Depends, HTTPException
from app.database.db_connection import get_db
from app.modules.producto.schemas.producto_schema import(
    ProductoCreate, ProductoUpdate, ProductoResponse
)
from app.modules.producto.services.producto_service import ProductoService

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

@router.get("/", response_model=list[ProductoResponse])
def listar_productos(db=Depends(get_db)):
    service = ProductoService(db)
    return service.listar()

@router.get("/{id}", response_model=ProductoResponse)
def obtener_productos(id: int, db=Depends(get_db)):
    service = ProductoService(db)
    producto = service.obtener(id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/")
def crear_producto(data: ProductoCreate, db=Depends(get_db)):
    service = ProductoService(db)
    resultado = service.registrar(
        data.intUnidadMedidaID, 
        data.intCategoriaID, 
        data.strNombre, 
        data.strCodigo, 
        data.strCodigoBarras, 
        data.strDescripcion, 
        data.decPrecio, 
        data.decCosto
    )
    return resultado

@router.put("/")
def actualizar_producto(data: ProductoUpdate, db=Depends(get_db)):
    service = ProductoService(db)
    return service.actualizar(
        data.intProductoID,
        data.intUnidadMedidaID, 
        data.intCategoriaID, 
        data.strNombre, 
        data.strCodigo, 
        data.strCodigoBarras, 
        data.strDescripcion, 
        data.decPrecio, 
        data.decCosto
    )

@router.put("/anular/{id}")
def anular_producto(id: int, db=Depends(get_db)):
    service = ProductoService(db)
    return service.anular(id)