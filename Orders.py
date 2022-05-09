from Order import Order
from Repository import repo


class _Orders():
    def __init__(self, conn):
        self._conn = conn
        self.id = 1

    def insert(self, order):
        self._conn.execute("""
               INSERT INTO orders (id, location, hat) VALUES (?, ?, ?)
           """, [order.id, order.location, order.hat])
        self._conn.commit()

    def find(self, order_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, location, hat FROM orders WHERE id = ?
        """, [order_id])
        return Order(*c.fetchone())

    def execute_orders(self, orders_file, summery_file):
        summery_list = []
        with open(orders_file) as orders:
            for order_line in orders:
                order = order_line.split(',')
                location = order[0].replace("\n", "")
                topping = order[1].replace("\n", "")
                supplier_id = repo.getFirstSupplier(topping)
                supplier = repo.getSupplier(supplier_id)
                hat_id = repo.getHatID(topping, supplier_id)
                o = Order(self.id, location, hat_id)
                self.insert(o)
                self.id += 1
                repo.updateHatQuantity(hat_id)
                line = str(topping) + ',' + str(supplier.name) + ',' + str(location) + "\n"
                summery_list.append(line)
            with open(summery_file, 'w') as summery:
                summery.writelines(summery_list)
