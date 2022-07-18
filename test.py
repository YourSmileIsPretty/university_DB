import psycopg2
from psycopg2 import sql
import sys

import psycopg2
import sys

con = None
fout = None

try:

    con = psycopg2.connect(
          database="testdb",
          user="postgres",
          password="qwe4464023",
          host="127.0.0.1",
          port="5432"
        )

    cur = con.cursor()

    cur.execute("CREATE TABLE cars(id SERIAL PRIMARY KEY, name VARCHAR(255), price INT)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Audi', 52642)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Mercedes', 57127)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Audi', 9000)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Volvo', 29000)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Audi', 350000)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Citroen', 21000)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Hummer', 41400)")
    cur.execute("INSERT INTO cars(name, price) VALUES('Volkswagen', 21600)")

        #SOLUTION ALL MY HEAD PROBLEMS!!!!!
    price_car = 41400
    request = ("COPY (SELECT name, price from cars WHERE price = {0} ) TO STDOUT WITH CSV DELIMITER '|'".format(price_car))
    with open ("cars.csv", 'w') as file:
        cur.copy_expert(request, file)


except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    sys.exit(1)

except IOError as e:

    print(f'Error {e}')
    sys.exit(1)

finally:

    if con:
        con.close()

    if fout:
        fout.close()
