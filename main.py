import sqlite3
import DBParser as parser
import sys
import Orders

con = sqlite3.connect(sys.argv[4])


# Main function
def main(*args):
    parser.parse(sys.argv[1])
    order = Orders._Orders(con)
    order.execute_orders(sys.argv[2], sys.argv[3])


# Main call
if __name__ == '__main__':
    main(sys.argv)
