from sqlalchemy import text

class InventarioActualService:
    def __init__(self, db):
        self.db = db
    
    def listar(selft):
        query = text("[dbo].[usp_InventarioActual_Listar]")
        result = selft.db.execute(query)
        return [dict(row._mapping) for row in result]
