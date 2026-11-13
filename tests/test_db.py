import sqlite3  # noqa


from contextlib import closing  
import pytest 

from db import  create_schema, save_calculation,recent_calculations


def test_recent_calculation_is_empty() -> None:
    with closing(sqlite3.connect(":memory:"))as connection: 
        create_schema(connection)
        row = recent_calculations(connection)  

    assert row == []

  
def test_verify_recent_calculation_elements() ->None:
    with closing(sqlite3.connect(":memory:"))as connection:
        create_schema(connection)

        row_id = save_calculation(
        connection, 40.0, 15.0, 2, 23.0, "2026-01-01T12:00:00Z" )

        row = recent_calculations(connection) 

    assert row_id == 1
    assert len(row) == 1
    assert row[0][:4] == (40.0, 15.0, 2, 23.0)

    
def test_recent_calculations_return_newest_five() -> None:
    with closing(sqlite3.connect(":memory:"))as connection:
        create_schema(connection)
        for amount in range (1, 7):
            save_calculation(
                connection,
                float(amount),
                10.0,
                1,
                float(amount) * 1.1,
                f"2026-11-12-{amount}-T00:00:00Z"

            )
            rows = recent_calculations(connection)

    assert len(rows) == 5

    assert [row[0] for row in rows] == [6.0, 5.0, 4.0, 3.0, 2.0]


def test_for_zero_is_rejected_in_people() -> None:
    with closing(sqlite3.connect(":memory:"))as connection:
        create_schema(connection)
        with pytest.raises(sqlite3.IntegrityError):
            connection.execute(
                """INSERT INTO bills
                (amount,tip_percentage,people,per_person,created_at)
                VALUES(?,?,?,?,?)""",
                (40.0, 10.0, 0, 0.0,"2026-11-12"),
            )