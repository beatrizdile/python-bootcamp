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
# c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@gmail.com')")

# insert multiple data
# many_customer = [('Wes', 'Brown', 'wes@gmail.com'),
#                  ('Jules', 'Snow', 'jules@gmail.com'),
#                  ('Mary', 'White', 'mary@gmail.com')]
#
# c.execute("INSERT INTO customers VALUES (?,?,?)", many_customer)


# update records (change the first name to Bob if last name is Elder and rowid is 1)
# *can't use quotation marks in rowid because it's an integer not string
c.execute("""UPDATE customers SET first_name = 'Larry'
            WHERE last_name = 'Elder' AND rowid = 1
    """)

# delete record
# c.execute("DELETE from customers WHERE rowid = 2")


# query the database
c.execute("SELECT rowid, * FROM customers")
# query using order by (ASC AND DESC)
# *DESC* to go from higher to lower
# *first_name* to go alphabetical order
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
c.execute("SELECT rowid, * FROM customers ORDER BY first_name")


# query specific data (only the items with Elder as last_name)
# c.execute("SELECT rowid, * FROM customers WHERE last_name = 'Elder'")


# c.fetchone()
# c.fetchmany(3)

# fetch the first item
# print(c.fetchone()[0])

# fetch all items
items = c.fetchall()
print(f"{items}\n")

# *the rowid becomes the item 0
for item in items:
    print(item[0], item[1], item[2], item[3])


# commit the cursor instructions
conn.commit()

# close connection
conn.close()
