import sqlite3


def create_schema(connection: sqlite3.Connection) -> None:
    """Creating  a Schema for data base """
    connection.execute(
        """CREATE TABLE IF NOT EXISTS bills (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        amount REAL NOT NULL CHECK (amount > 0),
        tip_percentage REAL NOT NULL CHECK (tip_percentage >= 0 ),
        people INTEGER NOT NULL CHECK (people > 0),
        per_person REAL NOT NULL CHECK (per_person >= 0),
        created_at TEXT NOT NULL
        ) STRICT
        """
                    )
    connection.commit()


def save_calculation(
        connection: sqlite3.Connection,
        name: str,
        amount: float,
        tip_percentage: float,
        people: int,
        per_person: float,
        created_at: str,

)-> int:
    """ Save all the  calculation to  bills table"""
    cursor = connection.execute(
        """INSERT INTO  bills 
        (name, amount, tip_percentage, people, per_person, created_at)
        VALUES(?,?,?,?,?,?)""",
        (name, amount, tip_percentage, people, per_person, created_at),
    )
    connection.commit()

    if cursor.lastrowid is None:
        raise RuntimeError("SQLite did not return the inserted row identifier")
    return cursor.lastrowid


def recent_calculations(connection: sqlite3.Connection ) -> list[tuple]:
    """Retrieve the five most recent bill insertions"""
    cursor = connection.execute(
    
        """SELECT amount, tip_percentage,people,per_person,created_at
        FROM bills ORDER BY id  DESC LIMIT 5"""
    )
    return cursor.fetchall()

