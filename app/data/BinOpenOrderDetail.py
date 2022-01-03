from app.utilities.response import json_serialize
from app.utilities.db_connection import binance_wrapper_db, get_identifier_filter

""" GLOBAL """
db = binance_wrapper_db()
bin_open_order_table = db.bin_open_order 

def delete_item( id ):
    """
    Delete item from open orders db

    Args:
        id - identifier
    """
    identifier = get_identifier_filter( id )
    return bin_open_order_table.delete_one( identifier )
#End

def get_item( id ):
    """
    Retrieve item from document through the id passed

    Args:
        id - identifier
    """
    identifier = get_identifier_filter( id )
    return bin_open_order_table.find_one( identifier )
#End

def insert_item( args ):
    """
    Insert items into db as docs
    Args: 
        args - (dict) of attributes from input 
    """
    return bin_open_order_table.insert_one( args )
#End

def update_item( id, args ):
    """
    Update attributes of a specific document

    Args:
        id   - id of document
        args - args to update for document
    """
    identifier = get_identifier_filter( id )

    if 'id' in args:
        del args['id']

    return bin_open_order_table.update_one( identifier, { "$set": args } )
#End

def upsert_item( identifier, args ):
    """
    Update or insert

    Args:
        identifier - bson objectified id
        args - args to update for document
    """
    return bin_open_order_table.update_one( identifier, { "$set": args }, upsert=True )
#End

