import Hat
import Repository
import Supplier
from Repository import repo


def parse(config_file):
    repo.create_tables()
    with open(config_file) as file:
        amounts = file.readline()
        amounts.strip()
        amount = amounts.split(',')
        hatsTypeAmount = int(amount[0])
        suppliersAmount = int(amount[1])

        for i in range(0, hatsTypeAmount):
            line = file.readline()
            line = line.split(",")
            hat = Hat.Hat(int(line[0]), str(line[1]).replace("\n",""), int(line[2]), int(line[3]))
            repo.Hats.insert(hat)
        for i in range(hatsTypeAmount, hatsTypeAmount + suppliersAmount):
            line = file.readline()
            line = line.split(",")
            sup = Supplier.Supplier(int(line[0]), str(line[1]).replace("\n",""))
            repo.Suppliers.insert(sup)

class DBparser:
    # def __init__(self):
    #     # DBparser = self

    pass
