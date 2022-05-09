import atexit
import sqlite3
import sys
import Hats
import Suppliers



class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect(sys.argv[4])
        self.Hats = Hats._Hats(self._conn)
        self.Suppliers = Suppliers._Suppliers(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
                CREATE TABLE hats (
                id          INT     PRIMARY KEY,
                topping     TEXT    NOT NULL,
                supplier    INT     NOT NULL,
                quantity    INT     NOT NULL,

                FOREIGN KEY(supplier)     REFERENCES supplier(id)
                );

                CREATE TABLE suppliers (
                id       INT     PRIMARY KEY,
                name     TEXT    NOT NULL
                );

                CREATE TABLE orders (
                id        INT     PRIMARY KEY,
                location  TEXT    NOT NULL,
                hat       INT     NOT NULL,
                
                FOREIGN KEY(hat)  REFERENCES hat(id)
                );
        """)

    def getHatQuantity(self, hat_id):
        return self.Hats.getQuantity(hat_id)

    def updateHatQuantity(self, hat_id):
        return self.Hats.updateQuantity(hat_id)

    def removeHat(self, hat_id):
        return self.Hats.removeHat(hat_id)

    def getSuppliersCount(self, topping_name):
        return self.Hats.getSuppliersCount(topping_name)

    def getFirstSupplier(self, topping_name):
        return self.Hats.getFirstSupplier(topping_name)

    def getSupplier(self, id):
        return self.Suppliers.find(id)

    def getHatID(self, topping, supplier):
        return self.Hats.getHatID(topping, supplier)

repo = _Repository()
atexit.register(repo._close)


