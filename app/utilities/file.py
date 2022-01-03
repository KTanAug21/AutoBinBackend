import json
from app.utilities.formatter import format_file_path

def read_file( file_path ):
    """
    Get content of a file

    Args:
        file_path - path to file

    Return:
        ( file content ) 
    """
    file = open(  
        format_file_path( file_path ),
        "r"
    )
    return file.read()
#End 

def json_read_file( file_path ):
    """
    Read a json file

    Args:
        file_path - path to file

    Return:
        dict or list
    """
    return json.loads( read_file( file_path ) )
#End