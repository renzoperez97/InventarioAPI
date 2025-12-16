from sqlalchemy import text

class InventarioMovimientoService:
    def __init__(self, db):
        self.db = db

    def listar_movimientos(self, productoID: int, almacenID: int):
        query = text("""
            EXEC [dbo].[usp_InventarioMovimiento_Listar] 
                @intProductoID = :productoID, 
                @intAlmacenID =:almacenID
        """)
        result = self.db.execute(query, {"productoID": productoID, "almacenID": almacenID})
        return [dict(row._mapping) for row in result]

    def registrar(self, productoID: int, almacenID: int, tipoMovimiento: str, cantidad: float, costoUnitario: float, documentoRef: str, obs: str):
        query = text("""
           EXEC [dbo].[usp_InventarioMovimiento_Insertar]
                @intProductoID = :productoID,
                @intAlmacenID = :almacenID,
                @strTipoMovimiento = :tipoMovimiento,
                @decCantidad = :cantidad,
                @decCostoUnitario = :costoUnitario,
                @strDocumentoRef = :documentoRef,
                @strObservacion = :obs
        """)

        self.db.execute(query, {
            "productoID": productoID,
            "almacenID": almacenID,
            "tipoMovimiento": tipoMovimiento,
            "cantidad": cantidad,
            "costoUnitario": costoUnitario,
            "documentoRef": documentoRef,
            "obs": obs
        })

        self.db.commit()

        return {"mensaje": "Registrado correctamente"}
