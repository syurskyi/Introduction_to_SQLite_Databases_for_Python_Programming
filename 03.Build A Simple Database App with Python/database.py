import sqlite3


# Query The DB and Return All Records

def show_all():
    # connect to database
    conn = sqlite3.connect('customer.db')

    # Create a cursor
    c = conn.cursor()

    # Query The Database
    c.execute("SELECT rowid, * FROM customers")

    items = c.fetchall()

    for item in items:
        print(item)

    # Commit our command
    conn.commit()

    # Close our connection
    conn.close()

# Add a New Record to the Table


def add_one(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?, ?, ?)", (first, last, email))
    conn.commit()
    conn.close()