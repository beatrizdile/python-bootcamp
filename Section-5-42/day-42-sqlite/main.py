import sqlite3

# make connection
conn = sqlite3.connect("customer.db")

# create cursor
c = conn.cursor()

# create table
# c.execute("""CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email text
#     )""")

# insert
c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@gmail.com')")

# insert multiple data
# many_customer = [('Wes', 'Brown', 'wes@gmail.com'),
#                  ('Jules', 'Snow', 'jules@gmail.com'),
#                  ('Mary', 'White', 'mary@gmail.com')]
#
# c.execute("INSERT INTO customers VALUES (?,?,?)", many_customer)

# query the database
c.execute("SELECT * FROM customers")
# c.fetchone()
# c.fetchmany(3)

print(c.fetchall())

# commit
conn.commit()

# close connection
conn.close()
