import sqlite3

with sqlite3.connect("roster.db") as conn:
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Roster(
            Name TEXT,
            Species TEXT,
            Age INTEGER
        )
    """)

    cursor.executemany("""
        INSERT INTO Roster (Name, Species, Age)
        VALUES (?, ?, ?)
    """, [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ])

    cursor.execute("""
        UPDATE Roster 
        SET Name = 'Ezri Dax' 
        WHERE Name = 'Jadzia Dax'
    """)

    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("DELETE FROM Roster WHERE Age > 100")


