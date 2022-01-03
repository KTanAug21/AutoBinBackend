from app.utilities.response import json_serialize
from app.utilities.db_connection import binance_wrapper_db

""" GLOBAL """
db = binance_wrapper_db()
bin_open_order_table = db.bin_open_order 

def get_db_list( ):
    """
    Get the list of orders from the bin open order collection
    """
    return json_serialize( bin_open_order_table.find({}) ) 
#End