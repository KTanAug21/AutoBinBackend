from app.data.utilities.bin_connection import get_binance_client
from app.data.BinOpenOrderLiveList import get_open_orders
from app.controllers.PairPreferenceList import sup_pair_name_list

""" BinOpenrOrderLiveList """

def get_list():
    """
    resource: BinOpenrOrderLiveList.get
    """

    print( 'Connecting to Bin client' )
    client = get_binance_client()
    
    # Get Pair Names as a list
    pair_names_list = sup_pair_name_list()
    return pair_names_list
    print( 'Processing each item in the list {}'.format( pair_names_list ) ) 
    for symbol in pair_names_list:
        print( 'Getting pair {}'.format(symbol) )
        orders = get_open_orders( client, symbol, False )
    #End
    
    print( 'Returning result' )
    return orders
    
#End 
