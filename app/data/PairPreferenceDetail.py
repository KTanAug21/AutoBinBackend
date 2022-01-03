from app.utilities.response import json_serialize
from app.utilities.db_connection import binance_wrapper_db, get_identifier_filter
from app.utilities.date_time import current_ms_time

""" GLOBAL """
db = binance_wrapper_db()
pair_preference_table = db.pair_preference 

def delete_item( id_filter ):
    """
    Delete directly from the db

    Args:
        id_filter - bson objectified id
    """
    return pair_preference_table.delete_one( id_filter )
#End

def get_item( id_filter ):
    """
    Retrieve directly from the db
    
    Args:
        id_filter - bson objectified id
    """

    return pair_preference_table.find_one( id_filter )
#End

def get_item_by_symbol( pair ):
    """
    Retrieve item from document through the symbol passed

    Args:
        pair - identifier
    """

    return pair_preference_table.find_one( {'pair':pair} )
#End

def insert_item( args ):
    """
    Insert directly to the db
    
    Args:
        args - args of new doc to create
    """

    return pair_preference_table.insert_one( args )
#End

def update_item( id, args ):
    """
    Update Item directly in the db

    Args:
        id - id of document to update
        args - attributes to update in the doc
    """
    
    # Format id identifier
    identifier = get_identifier_filter( args['id'] )

    # Identifier object
    if 'id' in args:
        del args['id']

    if 'synced_at' in args and args['synced_at'] is None:
        del args['synced_at']

    args['updated_at'] = current_ms_time()
    return pair_preference_table.update_one( identifier, { "$set": args } )
#End
