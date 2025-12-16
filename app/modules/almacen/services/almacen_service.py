from sqlalchemy import text

class AlmacenService:
    def __init__(self, db):
        self.db = db

    def listar(self):
        query = text("EXEC [dbo].[usp_Almacen_Listar]")
        result = self.db.execute(query)
        return [dict(row._mapping) for row in result]

    def obtener(self, id: int):
        query = text("EXEC [dbo].[usp_Almacen_Obtener] :id")
        row = self.db.execute(query, {"id": id}).fetchone()
        return dict(row._mapping) if row else None

    def registrar(self, nombre: str, direccion: str):
        query = text("""
            EXEC [dbo].[usp_Almacen_Insertar] 
                @strNombre = :nombre,
                @strDireccion = :direccion
        """)

        self.db.execute(query, {
            "nombre": nombre,
            "direccion": direccion
        })

        self.db.commit()

        return {"mensaje": "Registrado correctamente"}


    def actualizar(self, id: int, nombre: str, direccion: str):
        query = text("""
            EXEC [dbo].[usp_Almacen_Actualizar]
                @intAlmacenID = :id,
                @strNombre = :nombre,
                @strDireccion = :direccion
        """)

        self.db.execute(query, {
            "id": id,
            "nombre": nombre,
            "direccion": direccion
        })

        self.db.commit()

        return {"mensaje": "Actualizado correctamente"}


    def anular(self, id: int):
        query = text("""
            EXEC [dbo].[usp_Almacen_Anular]
                @intAlmacenID = :id
        """)

        self.db.execute(query, {"id": id})
        self.db.commit()

        return {"mensaje": "Almacén anulado correctamente"}
