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