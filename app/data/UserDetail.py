from app.data.utilities.date_time import current_ms_time, several_days_from_date_in_ms_time
from app.data.utilities.db_connection import binance_wrapper_db, get_identifier_filter
from app.data.utilities.response import json_serialize
from app.data.utilities.encryption_handler import jwt_encode


""" GLOBAL """
db = binance_wrapper_db()
user_table = db.user 

def insert_item( args ):
    """
    Insert items into db as docs
    Args: 
        args - (dict) of attributes from input 
    """
    return user_table.insert_one( args )
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

    return user_table.update_one( identifier, { "$set": args } )
#End

def generate_user_jwt_token( hashed_password ):
    """
    Generate JWT Token to be used for authentication
    
    Args:
        hashed_password - hashed password of the user, used as the secret to the jwt token
    
    Return:
        String - generated jwt tokenqa
    """
    # Generate Payload
    payload = generate_user_jwt_payload()
    return jwt_encode( payload, hashed_password )
#End

def extract_user_payload_from_jwt_token( user ):
    """
    Extract payload from jwt token
    
    Args:
        user - (dict) user instance to check, requires:    
            -token
            -password
    """
    return jwt_decode( user["token"], user["password"] )
#End

def generate_user_jwt_payload():
    """
    Generate Payload to be encoded as part of a user's jwt token
    
    Args:
        None

    Return:
        payload
    """
    current_date_ms = current_ms_time()
    number_of_days_expiry = 7
    
    return {
        "created_at" : current_date_ms,
        "expires_at" : several_days_from_date_in_ms_time( current_date_ms, number_of_days_expiry )
    }
#End

def get_user_by_email( email ):
    """
    Retrieve user by email
    Args:
        email - Identify user by email
    """
    return user_table.find_one( {"email":email} )
#End
