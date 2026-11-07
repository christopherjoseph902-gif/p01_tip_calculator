import sqlite3

def create_schema(connection: sqlite3.Connection) -> None:
    """Creating  a Schema for data base """
    connection.execute(
        """CREATE TABLE IF NOT EXIST bills (
        id INTEGER PRIMARY KEY,
        amount REAL NOT NULL CHECK (amount > 0),
        tip_pecentage REAL NOT NULL CHECK (tip_pecenatge >= 0 ),
        people INTEGER NOT NULL CHECK (people > 0),
        per_person REAL NOT NULL CHECK (per_person >= 0),
        created_at TEXT NOT NULL
        ) STRICT
        """
                    )
    connection.commit()

def save_calculation(
        connection: sqlite3.Connection,
        amount: float,
        tip_percentage: float,
        people: int,
        per_person: float,
        created_at: str,

)-> int:
    """ Save all the  calcualtoin to  bills table"""
    cursor = connection.execute(
        """INSERT INTO  bills 
        (amount,tip_percentage,people,per_person,created_at)
        VALUE(?,?,?,?,?)"""
        (amount,tip_percentage,people,per_person,created_at),
    )
    connection.commit()
    if cursor.lastrowid is None:
        raise RuntimeError("SQLite did not return the inserted row identifier")
    return cursor.lastrowid


def recent_calculations(connection: sqlite3.Connection ) -> list[tuple]:
    """Retrive the five most recent bill insertions"""
    cursor = connection.execute(
        """SELECT amount, tip_percentage,people,per_person,created_at
        FROM bills ORDER BY id  DESC LIMIT 5"""
    )
    return cursor.fetchall()