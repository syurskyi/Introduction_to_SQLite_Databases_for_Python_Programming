import database

# add a record to the database,
# database.add_one("Laura", "Smith", "laura@smith.com")

# Delete records use
# database.delete_one('7')

# Add many records

stuff = [
    ('Brenda', 'Smitherton', 'brenda@smitherton.com'),
    ('Joshua', 'Raintree', 'josh@raintree.com')
    ]

database.add_many(stuff)

# show all
database.show_all()