from app.schema.UserDetail import abort_get_user_detail_args, abort_put_user_detail_args, parse_get_user_detail_args, parse_put_user_detail_args, trans_put_user_detail_args, validate_password_matches_user_hash, validate_token_available_and_valid 
from app.data.local.handler import get_local_key
from app.data.UserDetail import generate_user_jwt_token, get_user_by_email, insert_item


def put_user_detail():
    """ 
    Validate args through schema
    Transform args to be db ready through schema
    Directly add transformed args to db through data
    """

    # Validate args
    args = parse_put_user_detail_args().parse_args()

    # Abort if necessary
    abort_put_user_detail_args( args )

    # Transform before put
    args = trans_put_user_detail_args( args )
    
    result = insert_item( args )
    
    return { "message" : get_local_key( "complete_add", "en" ) }
#End

 
def get_user_detail():
    """
    Get User details:
        if token:
            user id, name, email

        if  email, password, and, token_request
            token 
    """

    # VALIDATION
    args = parse_get_user_detail_args( ).parse_args()
    abort_get_user_detail_args( args )

    # EVENT
    if "token_request" in args:
        
        user = get_user_by_email( args['email'] )
     
        # Check password matches
        if validate_password_matches_user_hash( user["password"], args["password"] ):

            # Get JWT Token
            if validate_token_available_and_valid( user ):
                print( "token received" )
                token = user["token"]
            else:
                print( "token generated" )
                token = generate_user_jwt_token( user["password"] ) 
                
                # Update user with new token
                update_item( user['id'], ['token'] )
            #End

            # Respond
            return {
                "token" : token
            }
        else:
            abort( 422, message={'error':'Invalid user or password'} )

    return { "okay" : "okay" }
#End