"""
Defines the tables for the app.
"""

import datetime
import os

from peewee import *

DB_DIR = 'db'
DB_NAME = 'ethgas.db'
DB_PATH = os.path.join(DB_DIR, DB_NAME)

db = SqliteDatabase(DB_PATH)

class Gas(Model):
    created_at = DateTimeField(default=datetime.datetime.now)
    gas_price_fast = FloatField()
    gas_price_fastest = FloatField()
    gas_price_safe_low = FloatField()
    gas_price_average = FloatField()
    block_time = FloatField()
    block_num = FloatField()
    speed = FloatField()
    safe_low_wait = FloatField()
    average_wait = FloatField()
    fast_wait = FloatField()
    fastest_wait = FloatField()

    class Meta:
        database = db
