def ext_attr_from_dict_as_list( dict, key, get_unique = False ):
    """
    Extract specific attribute from a list of objects ( dict )

    Args: 
        dict - to extract from
        key  - attribute name to retrieve
        get_unique - determines whether list should contain unique items
        
    Return:
        final_list ( list )
    """
    final_list = []
    if get_unique:
        for item in dict:
            if key in item and item[key] not in final_list:
                final_list.append( item[ key ] )
    else:
        for item in dict:
            if key in item:
                final_list.append( item[ key ] )
    return final_list
#End

def format_file_path( file_name ):
    """
    Append relative file path to file name passed
    """
    return 'app/{}'.format(file_name)
#End