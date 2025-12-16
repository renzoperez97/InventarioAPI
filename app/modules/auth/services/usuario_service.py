from sqlalchemy import text

class UsuarioService:
    def __init__(self, db):
        self.db = db

    def validar_Usuario(self, usuario: str, clave: str):
        query = text("EXEC [dbo].[usp_UsuarioSistema_Login] @strUsuario= :strUsuario, @strClave = :strClave")
        result = self.db.execute(query, {"strUsuario": usuario, "strClave": clave})
        row = result.fetchone()

        if row:
            return {"strID": row.strID, "strMensaje": row.strMensaje}
        else:
            return {"strID": "0", "strMensaje": "Error al ejecutar el SP"}