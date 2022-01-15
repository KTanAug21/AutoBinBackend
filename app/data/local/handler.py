from app.data.local.constant import list_constant
from app.data.local.en import list_en


def get_local_key( key, list_name ):
    """
    Return value of a global constant
    Args 
        key       - identifier to be used in retrieving value from get_constant_dct
        list_name - identifier to be used in retrieving value
    """
    dict = get_option(list_name)
   
    if key in dict:
        return dict[key]
    else:
        return ''
    #End
#End


def get_option( list_name ):
    """
    Return options for listing
    Args:
        list_name - corresponds to list method to call

    Return:
        String ( list method ) 
    """
    options = {
        "constant":list_constant,
        "en":list_en
    }
    return options[list_name]()
#End