from flask_restful import Resource

from app.data.utilities.response import respond
from app.controllers.BinOpenOrderLiveList import get_list
from decorator import login_required

class BinOpenOrderLiveList( Resource ):
    @login_required
    def get( self ):
        """
        List pair preference documents
        """
        result = get_list()
        return respond( 200, result )
    #End
