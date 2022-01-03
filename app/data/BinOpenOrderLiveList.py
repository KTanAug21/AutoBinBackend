from app.utilities.file import json_read_file

def get_open_orders( client, symbol, from_json=False ):
    """
    Get a list of open orders for the specified symbol
    
    Args:
        client - connection to binance
        symbol - pair to get orders for
        from_json - determines whether to read from live client data or from sample json
            - bin_open_order_live_list.json

    Return:
        ( list )
    """
    if from_json:
        print( 'Reading from json file' )
        return json_read_file( 'data/json/bin_open_order_live_list.json' )
    else:
        print( 'Reading from client conn' )
        return  client.get_open_orders(symbol=symbol)
#End