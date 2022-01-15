from app.data.utilities.response import json_serialize
from app.data.utilities.db_connection import binance_wrapper_db, get_identifier_filter

""" GLOBAL """
db = binance_wrapper_db()
bin_open_order_table = db.bin_open_order 

class Model():
    