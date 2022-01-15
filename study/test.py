# Balanced Parenthesis
pair_list = [ 
    ['{','}'],
    ['[',']'],
    ['(',')']  
]

def is_balanced( string ):
    """
    Check whether string consists of balanced parenthesis
    Args:
        string - to check
    """
    stack = []
    # Loop through characters
    for c in string:
        # If character open add to stack ( append )
        if is_open_char( c ):
            print( 'Stacking {}'.format(c) )
            stack.append( c )
        else:
            print( 'Comparing {}'.format(c) )
            len_ = len(stack)
            open = stack.pop()
            if len_ == 0 or not open_matches_close( open, c ):
                # else check if not empty, check if matches current open 
                return False
    #End

    # If string is emptuy true
    return len(stack) == 0
#End

def is_open_char( char ):
    """
    Determine whether character is open or not
    Args:
        char - char
        O(n)
    """
    for pair in pair_list:
        if char == pair[0]:
            return True
    #End

    return False
#End

def open_matches_close( open, close ):
    """
    Determine whether two characters match the open and close of each other
    Args:
        open - open part
        close - close part
    """
    print( 'Checking {} {}'.format(open,close) )
    for pair in pair_list:
        if pair[0] == open:
            if pair[1] != close:
                return False
            else:
                return True
        elif pair[1] == close:
            if pair[0] != open:
                return False
            else:
                return True
    return False
#End

print( is_balanced( '{[]}[[]]([{}])' ) ) 
#print( is_open_char('{'))
#print( open_matches_close('(',')') )