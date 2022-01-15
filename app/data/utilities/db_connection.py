from bson.objectid import ObjectId
from flask_restful import abort
from pymongo import MongoClient
from app.data.utilities.date_time import current_ms_time
import os
import traceback

def binance_wrapper_db():
    """
    Connect to binance wrapper db
    """
    try:
        url   = os.getenv('MONGO_DB')
        mongo = MongoClient(url, serverSelectionTimeoutMS=5000)
        mongo.server_info() 
        return mongo.binance_wrapper
    except:
        print('checking')
        print( traceback.format_exc() )
        print('Unable to connect to db')
       
        return None
    #End
#End


def get_identifier_filter( id ):
    """
    Get Document Identifier through id
    
    Args:
        id - Objectify using bson
    """
    return {'_id': ObjectId(id)}
#End


