import sqlite3
conn = sqlite3.connect('library.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Library(
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
    )
""")

conn.commit()

cursor.executemany("""
    INSERT INTO Library(Title, Author, Year_Published, Genre)
    VALUES (?, ?, ?, ?)
""",[
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell	", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic"),
]
)
conn.commit()
cursor.execute("""
Update Library
Set Year_Published = 1950
where Title = "1984"
""")

cursor.execute("select Title, Author from Library where Genre = 'Dystopian'")
for row in cursor.fetchall():
    print(row)

cursor.execute("delete from Library where Year_Published < 150")
conn.commit()

cursor.execute("select * from Library order by Year_Published asc")
for row in cursor.fetchall():
    print(row)

conn.close()

