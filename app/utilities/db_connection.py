from bson.objectid import ObjectId
from flask_restful import abort
from pymongo import MongoClient
from app.utilities.date_time import current_ms_time

def binance_wrapper_db():
    """
    Connect to binance wrapper db
    """
    try:
        mongo  = env('MONGO_DB')
        mongo.server_info() 
        return mongo.binance_wrapper
    except:
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


