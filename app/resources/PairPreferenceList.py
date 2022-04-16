from flask_restful import Resource

from app.data.utilities.response import respond
from app.controllers.PairPreferenceList import get_pair_preference_list
from decorator import login_required

class PairPreferenceList( Resource ):

    @login_required
    def get( self ):
        """
        List pair preference documents
        """
        result = get_pair_preference_list()
        return respond( 200, result )
    #End
