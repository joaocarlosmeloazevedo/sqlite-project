import database

#database.add_one("Peter","Parker","peterparker@spiderman.com")

#Delete record use a rowid as a STRING
#database.delete_one('6')

stuff = [
    ('Drake', 'Bell', 'drakebell@nickelodeon.com'),
    ('Timmy', 'Turner', 'timmyturner@nickelodeon.com'),
    ('Sponge', 'Bob', 'spongebob@nickelodeon.com')
    ]

database.add_many(stuff)

database.show_all()


