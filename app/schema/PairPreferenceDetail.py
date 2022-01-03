from app.utilities.date_time import current_ms_time
from flask_restful import abort, reqparse


""" PairPreference DELETE """
def parse_delete_detail_args():
    """ 
    Use Detail validator 
    """
    return parse_get_detail_args()
#End

""" PairPreference GET """
def parse_get_detail_args():
    """
    Validate proper parameters passed 
    """
    parser = reqparse.RequestParser()
    parser.add_argument( "id", type=str, help="DB Identifier of the pair being requested", required=True )
    return parser
#End




""" PairPreference PUT"""
def parse_put_pair_preference_args():
    """
    Validate proper parameters passed 
    """
    parser = reqparse.RequestParser()
    parser.add_argument( "pair", type=str, help="Crypto pair to be monitored for open orders", required=True )
    parser.add_argument( "created_at" )
    return parser
#End


from app.data.PairPreferenceDetail import get_item_by_symbol;
def abort_put_pair_preference( args ):
    """
    Abort Adding if name already exists
    """

    # Get pair from db record
    db_record = get_item_by_symbol( args['pair'] )
    # Throw error if pair retrieved
    if db_record is not None:
        abort( 422, message={'pair':'Pair already exist...'} )

#End

def trans_put_pair_preference_args( args ):
    """
    Transform args before put action
    """
    args['created_at'] = current_ms_time()
    return args
    
#End


""" PairPreference PATCH"""
def parse_patch_pair_preference_args():
    """
    Validate proper parameters passed 
    """
    parser = reqparse.RequestParser()
    parser.add_argument( "id", type=str, help="DB Identifier of the pair being requested", required=True )
    parser.add_argument( "pair", type=str, help="Crypto pair to be monitored for open orders", required=True )
    parser.add_argument( "updated_at" )
    parser.add_argument( "synced_at" )
    return parser
#End



