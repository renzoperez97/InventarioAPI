from pydantic import BaseModel

class UsuarioLoginRequest(BaseModel):
    strUsuario: str
    strClave: str

class UsuarioLoginResponse(BaseModel):
    strID: str
    strMensaje: str
    token: str | None = None