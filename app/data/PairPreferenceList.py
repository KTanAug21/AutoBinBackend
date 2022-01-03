from app.utilities.response import json_serialize
from app.utilities.db_connection import binance_wrapper_db
from app.utilities.date_time import current_ms_time

""" GLOBAL """
db = binance_wrapper_db()
pair_preference_table = db.pair_preference 

def get_db_list( ):
    """
    Get all pair preferences from the db
    """
    return json_serialize( pair_preference_table.find({}) )
#End

def update_sync_db_list( ):
    """
    Update all pair preferences' synced_at date
    """
    pair_preference_table.update_many(
        {},
        {
            "$set": { "synced_at" :  current_ms_time() }
        }
    )
#End