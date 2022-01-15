import bcrypt


def encrypt_string( string ):
    """
    Encrypt string passed

    Args:
        string - get string to encrypt
    Return:
        String ( hashed ) 
    """
    encoded_string = string.encode()

    hash =  bcrypt.hashpw( encoded_string, bcrypt.gensalt())
    return hash
#End

def check_string_match_hash( string, hashed_string ):
    """
    Check if string passed matches the hashed string

    Args:
        string - normal string
        hashed_string - to check against
    Return:
        Boolean
    """
    encoded_string = string.encode()

    if bcrypt.checkpw( encoded_string, hashed_string ):
        return True
    else:
        return False
#End

import jwt
def jwt_encode( payload, secret ):
    """
    Encode given payload using secret
    in JWT format

    Args:
        payload - to encode
        secret  - its a secret
    Return:
        String
    """
    return jwt.encode( payload, secret, algorithm="HS256" )
#End

def jwt_decode( token, secret ):
    """
    Decode given jwt token

    Args:
        token - jwt token to decode
    Return:
        payload - passed payload that was encoded
    """
    return jwt.decode( token, secret, algorithms=["HS256"] )
#End