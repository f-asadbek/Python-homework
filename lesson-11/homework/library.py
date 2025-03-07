import sqlite3

def main():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # 1
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books (
        Title TEXT,
        Author TEXT,
        Year_Published INTEGER,
        Genre TEXT
    )
    """)

    # 2
    cursor.executemany("""
    INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)
    """, [
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
        ("1984", "George Orwell", 1949, "Dystopian"),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
    ])

    # 3
    cursor.execute("""
    UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'
    """)

    # 4
    cursor.execute("""
    SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'
    """)
    print("Dystopian books:", cursor.fetchall())

    # 5
    cursor.execute("""
    DELETE FROM Books WHERE Year_Published < 1950
    """)

    # 6
    cursor.execute("""
    ALTER TABLE Books ADD COLUMN Rating REAL
    """)

    rating_updates = {
        "To Kill a Mockingbird": 4.8,
        "1984": 4.7,
        "The Great Gatsby": 4.5
    }
    for title, rating in rating_updates.items():
        cursor.execute("""
        UPDATE Books SET Rating = ? WHERE Title = ?
        """, (rating, title))

    # 7
    cursor.execute("""
    SELECT * FROM Books ORDER BY Year_Published ASC
    """)
    print("Books sorted by Year Published (asc):", cursor.fetchall())

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
