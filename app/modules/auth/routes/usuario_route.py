from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db_connection import get_db
from app.modules.auth.services.usuario_service import UsuarioService
from app.modules.auth.schemas.usuario_schema import UsuarioLoginRequest, UsuarioLoginResponse
from app.modules.auth.security import crear_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=UsuarioLoginResponse)
def Login(request: UsuarioLoginRequest, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    usuario = service.validar_Usuario(request.strUsuario, request.strClave)

    if usuario["strID"] == "0":
        return usuario
    
    token = crear_token({
        "id": usuario["strID"],
        "usuario": request.strUsuario
    })

    usuario["token"] = token

    return usuario  