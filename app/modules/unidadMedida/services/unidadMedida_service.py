from sqlalchemy import text

class UnidadMedidaService:
    def __init__(self, db):
        self.db = db
    
    def listar(self):
        query = text("EXEC [dbo].[usp_UnidadMedida_Listar]")
        result = self.db.execute(query)
        return [dict(row._mapping) for row in result]
    
    def obtener(self, id: int):
        query = text("EXEC [dbo].[usp_UnidadMedida_Obtener] :id")
        row = self.db.execute(query, {"id": id}).fetchone()
        return dict(row._mapping) if row else None
    
    def registrar(self, nombre: str, abreviatura: str):
        query = text("""
            EXEC [dbo].[usp_UnidadMedida_Insertar]
                @strNombre = :nombre,
                @strAbreviatura = :abreviatura
        """)

        self.db.execute(query, {
            "nombre": nombre,
            "abreviatura": abreviatura,
        })

        self.db.commit()

        return {"mensaje": "Registrado correctamente"}


    def actualizar(self, id: int, nombre: str, abreviatura: str):
        query = text("""
            EXEC [dbo].[usp_UnidadMedida_Actualizar]
                @intUnidadMedidaID = :id,
                @strNombre = :nombre,
                @strAbreviatura = :abreviatura
        """)

        self.db.execute(query, {
            "id": id,
            "nombre": nombre,
            "abreviatura": abreviatura
        })

        self.db.commit()

        return {"mensaje": "Actualizado correctamente"}


    def anular(self, id: int):
        query = text("""
            EXEC [dbo].[usp_UnidadMedida_Anular]
                @intUnidadMedidaID = :id
        """)

        self.db.execute(query, {"id": id})
        self.db.commit()

        return {"mensaje": "Unidad de Medida anulado correctamente"}