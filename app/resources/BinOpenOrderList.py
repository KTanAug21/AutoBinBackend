from flask_restful import Resource

from app.data.utilities.response import respond
from app.controllers.BinOpenOrderList import get_list
from decorator import login_required

class BinOpenOrderList( Resource ):
    @login_required
    def get( self ):
        """
        List open order documents
        """
        result = get_list()
        return respond( 200, result )
    #End
 