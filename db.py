import sqlite3
from sqlite3 import Error
from models import db, Gas


def create_tables():
    try:
        print("connecting to db...")
        db.connect()
        print("creating gas table")
        db.create_tables([Gas])
        print("tables successfully created")
    except Exception as e:
        print(e)
        raise e


if __name__ == '__main__':
    create_tables()