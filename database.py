import sqlite3

# Query the Database and return all records.
def show_all():
    #Connect to database
    conn = sqlite3.connect("customer.db")
    #Create a cursor
    c = conn.cursor()
    #Query the database
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    #Looping and showing all the records.
    for item in items:
        print(item)

    #Commit to DB
    conn.commit()
    #Closing connecting
    conn.close()

# Add a new record to the table.
def add_one(first,last,email):
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES(?,?,?)", (first,last,email))
    conn.commit()
    conn.close()

#Delete a record from table
def delete_one(id):
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE rowid = ?", id)
    conn.commit()
    conn.close()

