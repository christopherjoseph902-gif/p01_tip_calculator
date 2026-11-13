from contextlib import closing #noqa
from functools import partial
from pathlib import Path
import sqlite3

from db import  create_schema, save_calculation
from tipcalc import run_calculator 


DB_PATH = Path(__file__).resolve().with_name("main.db")


if __name__ == "__main__":
    with closing(sqlite3.connect(DB_PATH)) as connection:
        create_schema(connection)

        save = partial(save_calculation,connection)

        run_calculator(input, print, save)
