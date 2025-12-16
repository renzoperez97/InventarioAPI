from sqlalchemy import text

class CategoriaService:
    def __init__(self, db):
        self.db = db
    
    def listar(self):
        query = text("EXEC [dbo].[usp_Categoria_Listar]")
        result = self.db.execute(query)
        return [dict(row._mapping) for row in result]
    
    def obtener(self, id: int):
        query = text("EXEC [dbo].[usp_Categoria_Obtener] :id")
        row = self.db.execute(query, {"id": id}).fetchone()
        return dict(row._mapping) if row else None
    
    def registrar(self, nombre: str, descripcion: str):
        query = text("""
            EXEC [dbo].[usp_Categoria_Insertar]
                @strNombre = :nombre,
                @strDescripcion = :descripcion
        """)

        self.db.execute(query, {
            "nombre": nombre,
            "descripcion": descripcion,
        })

        self.db.commit()

        return {"mensaje": "Registrado correctamente"}


    def actualizar(self, id: int, nombre: str, descripcion: str):
        query = text("""
            EXEC [dbo].[usp_Categoria_Actualizar]
                @intCategoriaID = :id,
                @strNombre = :nombre,
                @strDescripcion = :descripcion
        """)

        self.db.execute(query, {
            "id": id,
            "nombre": nombre,
            "descripcion": descripcion
        })

        self.db.commit()

        return {"mensaje": "Actualizado correctamente"}

    def anular(self, id: int):
        query = text("""
            EXEC [dbo].[usp_Categoria_Anular]
                @intCategoriaID = :id
        """)

        self.db.execute(query, {"id": id})
        self.db.commit()

        return {"mensaje": "Categoria anulado correctamente"}