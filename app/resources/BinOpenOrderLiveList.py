from flask_restful import Resource

from app.utilities.response import respond
from app.controllers.BinOpenOrderLiveList import get_list


class BinOpenOrderLiveList( Resource ):

    def get( self ):
        """
        List pair preference documents
        """
        result = get_list()
        return respond( 200, result )
    #End
