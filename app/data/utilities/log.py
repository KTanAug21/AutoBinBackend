import inspect

def log_validation_error( error ):
    """
    Print out the error message
    Determine method name

    Args:
        error - message to convey

    Return:
        error - message passed to function
    """
    try:
        caller = inspect.stack()[1][3]
    except:
        caller = ''
    #End

    print( 'Failed validation with error: "{}" :: {}'.format( error, caller ) )
    return error
#End