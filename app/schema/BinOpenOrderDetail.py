from app.utilities.date_time import current_ms_time
from flask_restful import abort, reqparse

""" DELETE """
def parse_delete_detail_args():
    """
    Validate with parse get detail
    """
    return parse_get_detail_args()
#End


"""  GET """
def parse_get_detail_args():
    """
    Validate proper parameters passed 
    """
    parser = reqparse.RequestParser()
    parser.add_argument( "id", type=str, help="DB Identifier of the open order being requested", required=True )
    return parser
#End

""" PUT """
def parse_put_detail_args():
    """
    Validate proper parameters passed 
    """
    parser = reqparse.RequestParser()
    parser.add_argument( "symbol", type=str, help="Crypto pair/symbol for the order", required=True )
    parser.add_argument( "orderId", type=str, help="Id from binance uniquely identifying the order", required=True )
    parser.add_argument( "clientOrderId", type=str, help="Id auto gen by binance or user identifying order", required=True )
    parser.add_argument( "price",  help="The price to process order", required=True )
    parser.add_argument( "origQty", help="Number of main symbol units to process", required=True )
    parser.add_argument( "status", type=str, help="Status of the order", required=True )
    parser.add_argument( "type", type=str, help="Type of trade requested", required=True )
    parser.add_argument( "side", type=str, help="Type of trade operation requested", required=True )
    parser.add_argument( "stopPrice", help="Triggers request for trade when the main unit reaches this price", required=True )
    parser.add_argument( "time", help="Timestamp when order was requeted",  )
    parser.add_argument( "created_at" )
    parser.add_argument( "updated_at" )
    return parser
#End

def trans_put_detail_args( args ):
    """
    Transform args before put action
    """
    args['created_at'] = current_ms_time()
    args['updated_at'] = args['created_at']

    return args
    
#End


""" PATCH """
def parse_patch_detail_args():
    parser = parse_get_detail_args()
    return parser
#End

def trans_patch_detail_args( args ):
    """
    Transform args before put action
    """
    args['updated_at'] = current_ms_time()

    return args
    
#End

def trans_patch_detail_args( args ):
    """
    Extracts relevant information from the args passed in the request

    Args:
        args - (dict) from request

    Return:
        to_insert_dict - (dict) of attributes to update document with

    """
    from_args = [ 
        'id',
        'symbol', 
        'orderId', 
        'clientOrderId', 
        'price', 
        'origQty',
        'status',
        'type',
        'side',
        'stopPrice',
        'time',
        'created_at',
        'reverse_price',
        'reverse_origQty',
        'reverse_stopPrice',
        'allow_trigger'
    ]
    
    # Retrieve available values
    to_insert_dict = {}
    for key in from_args:
        if key in args:
            to_insert_dict[key] = args[key]
        #End
    #End

    # Conditional attribute values
    if 'reverse_price' in to_insert_dict and 'allow_trigger' not in to_insert_dict:
        to_insert_dict['allow_trigger'] = True

    to_insert_dict['updated_at'] =  current_ms_time()
    return to_insert_dict
#End


