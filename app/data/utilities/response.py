def respond( status, result ):
    """
    Return dictionary for responding to web actions

    Args:
        status - status of result
        result - details from result
    """
     
    if status < 300 and status >= 200:
        message = "Success"
    else:
        message = "Unable to process request"
    return {"status":status,"message": message,"data":result}, status
#End

import json
import bson.json_util as json_util
def json_serialize( args ):
    """
    Return args as a json serialized string

    Args
        args - args
    """
    return json.loads( 
        json_util.dumps(
            args
        )
    )
#End

def error_json( err_json ):
    """
    Standard error response

    Args:
        err_json - error message
    """
    return {
        "message": 
        err_json 
    }
#End