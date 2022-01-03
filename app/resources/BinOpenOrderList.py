from flask_restful import Resource

from app.utilities.response import respond
from app.controllers.BinOpenOrderList import get_list


class BinOpenOrderList( Resource ):

    def get( self ):
        """
        List open order documents
        """
        result = get_list()
        return respond( 200, result )
    #End
 