from app.schema.BinOpenOrderDetail import parse_delete_detail_args
from app.data.BinOpenOrderDetail import delete_item
def delete_detail():
    """
    Delete order from db business logic
    """

    # Validate args
    args   = parse_delete_detail_args().parse_args()
    result = delete_item( args['id'] )
    return { 'message':'Completed Delete' }
#End

from app.data.utilities.response import json_serialize
from app.data.BinOpenOrderDetail import get_item
from app.schema.BinOpenOrderDetail import parse_get_detail_args
from flask import request
def get_detail():
    """
    resource: BinOpenOrderDetail.get
    """
    # Validate args
    args   = parse_get_detail_args().parse_args()
    result = get_item( args['id'] )
    return json_serialize( result )
#End


from app.data.BinOpenOrderDetail import update_item
from app.schema.BinOpenOrderDetail import parse_patch_detail_args, trans_patch_detail_args
def patch_detail( ):
    """

    resource: BinOpenOrderDetail.put
    Update specific attributes of a document

    """
    
    # Validate args
    parse_patch_detail_args().parse_args()

    # Transform args
    args = request.json 
    args = trans_patch_detail_args( args )

    # Update instance
    result = update_item( args['id'], args )

    return { 'message':'Completed Update' }
    
    
#End






