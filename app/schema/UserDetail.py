from flask_restful import abort, reqparse
from app.data.local.handler import get_local_key
from app.data.UserDetail import extract_user_payload_from_jwt_token
from app.data.utilities.date_time import current_ms_time
from app.data.utilities.log import log_validation_error
from app.data.utilities.encryption_handler import encrypt_string

""" GENERAL """
import re
def validate_email_pattern( email ):
    """
    Validate if string provided contains valid email pattern
    Args:
        email - string to check

    Return:
        Boolean ( True ) or
        String ( Validation Error )
    """

    print( 'Checking email {}'.format(email) )
    regex_email_pattern  = get_local_key( "regex_email_pattern", "constant" )
    print( 'Validating with regex: {}'.format( regex_email_pattern ) )

    if not re.match( regex_email_pattern, email ):
        error = get_local_key( "er_email_pattern", "en")
        return log_validation_error( error )
    else:
        return True
#End

def validate_user_already_exist_through_email( email ):
    """
    Validate whether a user account exists for an email
    Args:
        email - email to find a user account for
    Return:
        Boolean ( True )
        String ( Validation Error )
    """
    # Validate email unique
    db_record = get_user_by_email( email )
    if db_record is None:
        return False
    else:
        return True
    #End
#End

from app.data.utilities.encryption_handler import check_string_match_hash
def validate_password_matches_user_hash( hashed, password ):
    """
    Validate whether the password passed 
    in the argument matches the hashed password stored in the db
    
    Args:
        hashed - hashed password stored in db
        password - string to match with hashed
    Return:
        Boolean
    """
    if check_string_match_hash( password, hashed ):
        return True
    else:
        return False
#End

def validate_token_available_and_valid( user ):
    """
    Check whether jwt token is present in user instance
    and if it is still valid

    Args:
        user - (dict) instance of user

    Return:
        Boolean
    """
    if 'token' in user and not user['token'] is None:
    
        # Decode jwt token
        decoded = extract_user_payload_from_jwt_token( user )
        print( decoded )
        if 'expires_at' in decoded:

            current_date_ms = current_ms_time()
            if current_date_ms <= decoded['expires_at']:
                return True
            #End
            
        #End

    #End
    return False
#End

""" GET """
def abort_get_user_detail_args( args ):
    """
    Abort put if there is an issue with args
    Args: 
        args - args to check 

    Return:
        None
    """
    error = {}
    if 'id' not in args or args['id'] is None:
        if 'email' not in args or args['email'] is None:
            abort( 422, message={'email':log_validation_error( 'Please provide the id of the User.' )} )
        elif 'password' not in args or args['password'] is None:
            abort( 422, message={'password':log_validation_error( 'Please provide the password of the User.' )} )
    #End

    # Validate email
    if 'token_request' in args and args['token_request']:
        
        if 'email' in args and args['email'] is not None:
            result = validate_email_pattern( args['email'] )
            if not result == True:
                abort( 422, message={'email':result} )

            # Validate email exist
            result = validate_user_already_exist_through_email( args['email'] )
            if not result :
                error = get_local_key( "er_email_user_does_not_exist", "en" )
                abort( 422, message={'email':log_validation_error( error )} )
            #End
        #End
    #End
#End

def parse_get_user_detail_args():
    """
    Validate proper parameters passed 
    """
    parser = reqparse.RequestParser()
    parser.add_argument( "id", type=str, help="Email address of user" )
    parser.add_argument( "email", type=str, help="Email address of user" )
    parser.add_argument( "password", type=str, help="Password of user" )
    parser.add_argument( "token_request", type=bool, help="Request for token or not" )

    return parser
#End

def trans_get_user_detail_args( args ):
    """
    Transform args to be db insert/put ready

    Args:
        args - args from input 
    """
   
    args['password'] = encrypt_string( args['password'] )
   
    return args
#End 



""" PUT """
from app.data.UserDetail import get_user_by_email
def abort_put_user_detail_args( args ):
    """
    Abort put if there is an issue with args
    Args: 
        args - args to check 

    Return:
        None
    """
    error = {}
    
    # Validate email
    result = validate_email_pattern( args['email'] )
    if not result == True:

        abort( 422, message={'email':result} )

    else:
        
        # Validate email unique
        result = validate_user_already_exist_through_email( args['email'])
        if result == True:
            error = get_local_key( "er_email_user_exist", "en" )
            abort( 422, message={'email':log_validation_error( error )} )
        #End

    #End
#End

def trans_put_user_detail_args( args ):
    """
    Transform args to be db insert/put ready

    Args:
        args - args from input 
    """
   
    args['password'] = encrypt_string( args['password'] )
   
    return args
#End 

def parse_put_user_detail_args():
    """
    Validate proper parameters passed 
    """
    parser = reqparse.RequestParser()
    parser.add_argument( "email", type=str, help="Email address of user", required=True )
    parser.add_argument( "first_name", type=str, help="First Name of user", required=True )
    parser.add_argument( "last_name", type=str, help="Last Name of user", required=True )
    parser.add_argument( "password", type=str, help="Password", required=True )

    return parser
#End







