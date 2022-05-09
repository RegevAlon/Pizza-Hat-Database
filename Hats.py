from Hat import Hat


class _Hats:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, Hat):
        self._conn.execute("""
               INSERT INTO hats (id, topping, supplier, quantity) VALUES (?, ?, ?, ?)
           """, [Hat.id, Hat.topping, Hat.supplier, Hat.quantity])
        self._conn.commit()


    def find(self, hat_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, topping, supplier, quantity FROM hats WHERE id = ?
        """, [hat_id])
        return Hat(*c.fetchone())

    def getQuantity(self, hat_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT quantity From hats WHERE id = ?
                """,[hat_id])
        return c.fetchone()[0]

    def updateQuantity(self, hat_id):
        q = self.getQuantity(hat_id)
        c = self._conn.cursor()
        c.execute("""
            UPDATE hats SET quantity=(?) WHERE id=(?)
        """,[q-1,hat_id])
        self._conn.commit()
        if self.getQuantity(hat_id)==0:
            self.removeHat(hat_id)


    def removeHat(self, hat_id):
        c = self._conn.cursor()
        c.execute("""
            DELETE FROM hats WHERE id=(?)
        """,[hat_id])
        self._conn.commit()

    def getSuppliersCount(self, topping_name):
        c = self._conn.cursor()
        c.execute("""
                    SELECT COUNT(*) FROM hats WHERE topping = (?)
                """, [topping_name])
        return c.fetchone()[0]

    def getFirstSupplier(self, topping_name):
        c = self._conn.cursor()
        c.execute("""
                    SELECT min(supplier) FROM hats WHERE topping = (?)
                """, [topping_name])
        return c.fetchone()[0]

    def getHatID(self,topping,supplier):
        c = self._conn.cursor()
        c.execute("""
                    SELECT id FROM hats WHERE topping = (?) AND supplier=(?)
                """, [topping,supplier])
        return c.fetchone()[0]
        

