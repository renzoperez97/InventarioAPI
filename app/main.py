from fastapi import FastAPI, Depends
from app.modules.auth.routes.usuario_route import router as usuario_router
from app.modules.almacen.routes.almacen_route import router as almacen_router
from app.modules.producto.routes.producto_route import router as producto_router
from app.modules.inventarioactual.routes.inventarioActual_route import router as inventarioActual_router
from app.modules.inventarioMovimiento.routes.inventarioMovimiento_route import router as inventerioMovimiento_router
from app.modules.unidadMedida.routes.unidadMedida_route import router as unidadMedida_router
from app.modules.categoria.routes.categoria_route import router as categoria_router

app = FastAPI(title = "INVENTARIO.API")

app.include_router(usuario_router)
app.include_router(almacen_router)
app.include_router(producto_router)
app.include_router(inventarioActual_router)
app.include_router(inventerioMovimiento_router)
app.include_router(unidadMedida_router)
app.include_router(categoria_router)
