from flask_restful import Resource

from app.data.utilities.response import respond
from app.controllers.BinOpenOrderDetail import delete_detail, get_detail, patch_detail
from decorator import login_required

"""
Open Orders stored in db
"""
class BinOpenOrderDetail( Resource ):

    @login_required
    def delete( self ):
        """
        Delete open order document
        """
        result = delete_detail()
        return respond( 200, result )
    #End

    @login_required
    def get( self ):
        """
        Retrieve open order document
        """
        result = get_detail()
        return respond( 200, result )
    #End

    @login_required
    def patch( self ):
        """
        Update details of an existing detail
        """
        result = patch_detail()
        return respond( 200, result )
    #End

#End
