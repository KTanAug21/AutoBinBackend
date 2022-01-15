from app.data.utilities.db_connection import  get_identifier_filter
from app.data.utilities.response import json_serialize



""" PairPreferenceDetail """
from app.schema.PairPreferenceDetail import parse_delete_detail_args
from app.data.PairPreferenceDetail import delete_item
def delete_detail():
    """
    resource: PairPreferenceDetail.delete
    """
    # Validate args - use the get pair to validate if id avaialble
    args = parse_delete_detail_args().parse_args()
    delete_item( get_identifier_filter(args['id']) )
    return 'Deleted'
#End


from app.schema.PairPreferenceDetail import parse_get_detail_args
from app.data.PairPreferenceDetail import get_item
def get_detail():
    """
    resource: PairPreferenceDetail.get
    """
    # Validate args
    args = parse_get_detail_args().parse_args()
    result = get_item( get_identifier_filter(args['id']) )
    return json_serialize( result )
#End

from app.schema.PairPreferenceDetail import abort_put_pair_preference, parse_put_pair_preference_args, trans_put_pair_preference_args
from app.data.PairPreferenceDetail import insert_item
def put_pair_preference( ):
    """
    resource: PairPreferenceDetail.put
    """
    # Validate args
    args = parse_put_pair_preference_args().parse_args()

    # Abort for any args invalidity
    abort_put_pair_preference( args )

    # Transform before put
    args = trans_put_pair_preference_args( args )
    
    # Insert 
    print( 'Adding' )
    result = insert_item( args ) 

    return { 'message':'Completed Adding' }
#End

from app.schema.PairPreferenceDetail import abort_put_pair_preference, parse_put_pair_preference_args, parse_patch_pair_preference_args
from app.data.PairPreferenceDetail import update_item
def patch_pair_preference( ):
    """ 
    resource: PairPreferenceDetail.patch
    """
    # Validate args
    args = parse_patch_pair_preference_args().parse_args()

    # Abort for any args invalidity
    abort_put_pair_preference( args )

    # Update instance
    result = update_item( args['id'], args )
  
    return { 'message':'Completed Update' }

#End




