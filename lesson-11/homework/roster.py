import sqlite3

def main():
    conn = sqlite3.connect("roster.db")
    cursor = conn.cursor()

    # 1
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
    """)

    # 2
    cursor.executemany("""
    INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
    """, [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ])

    # 3
    cursor.execute("""
    UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'
    """)

    # 4
    cursor.execute("""
    SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
    """)
    print("Characters with Species 'Bajoran':", cursor.fetchall())

    # 5
    cursor.execute("""
    DELETE FROM Roster WHERE Age > 100
    """)

    # 6
    cursor.execute("""
    ALTER TABLE Roster ADD COLUMN Rank TEXT
    """)


    rank_updates = {
        "Benjamin Sisko": "Captain",
        "Ezri Dax": "Lieutenant",
        "Kira Nerys": "Major"
    }
    for name, rank in rank_updates.items():
        cursor.execute("""
        UPDATE Roster SET Rank = ? WHERE Name = ?
        """, (rank, name))

    # 7
    cursor.execute("""
    SELECT * FROM Roster ORDER BY Age DESC
    """)
    print("Characters sorted by Age (desc):", cursor.fetchall())


    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
