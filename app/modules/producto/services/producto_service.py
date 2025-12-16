from sqlalchemy import text

class ProductoService:
    def __init__(self, db):
        self.db = db

    def listar(self):
        query = text("EXEC [dbo].[usp_Producto_Listar]")
        result = self.db.execute(query)
        return [dict(row._mapping) for row in result]
    
    def obtener(self, id: int):
        query = text("EXEC [dbo].[usp_Producto_Obtener] :id")
        row = self.db.execute(query, {"id": id}).fetchone()
        return dict(row._mapping) if row else None
    
    def registrar(self, unidadMedidaID: int, categoriaID: int, nombre: str, codigo: str, codigoBarra: str, descripcion: str, precio: float, costo: float):
        query = text("""
            EXEC [dbo].[usp_Producto_Insertar]
                @intUnidadMedidaID = :unidadMedidaID,
                @intCategoriaID = :categoriaID,
                @strNombre = :nombre,
                @strCodigo = :codigo,
                @strCodigoBarras = :codigoBarra,
                @strDescripcion = :descripcion,
                @decPrecio = :precio,
                @decCosto = :costo
        """)

        self.db.execute(query, {
            "unidadMedidaID": unidadMedidaID,
            "categoriaID": categoriaID,
            "nombre": nombre,
            "codigo": codigo,
            "codigoBarra": codigoBarra,
            "descripcion": descripcion,
            "precio": precio,
            "costo": costo
        })

        self.db.commit()

        return {"mensaje": "Registrado correctamente"}
    
    def actualizar(self, id:int, unidadMedidaID: int, categoriaID: int, nombre: str, codigo: str, codigoBarra: str, descripcion: str, precio: float, costo: float):
        query = text("""
            EXEC [dbo].[usp_Producto_Actualizar]
                @intProductoID = :id,
                @intUnidadMedidaID = :unidadMedidaID,
                @intCategoriaID = :categoriaID,
                @strNombre = :nombre,
                @strCodigo = :codigo,
                @strCodigoBarras = :codigoBarra,
                @strDescripcion = :descripcion,
                @decPrecio = :precio,
                @decCosto = :costo
        """)

        self.db.execute(query, {
            "id": id,
            "unidadMedidaID": unidadMedidaID,
            "categoriaID": categoriaID,
            "nombre": nombre,
            "codigo": codigo,
            "codigoBarra": codigoBarra,
            "descripcion": descripcion,
            "precio": precio,
            "costo": costo
        })
        
        self.db.commit()

        return {"mensaje": "Actualizado correctamente"}
    
    def anular(self, id: int):
        query = text("""
            EXEC [dbo].[usp_Producto_Anular]
                @intProductoID = :id
        """)

        self.db.execute(query, {"id": id})
        self.db.commit()

        return {"mensaje": "Producto anulado correctamente"}