from flask_restful import Resource

from app.utilities.response import respond
from app.controllers.PairPreferenceList import get_pair_preference_list


class PairPreferenceList( Resource ):

    def get( self ):
        """
        List pair preference documents
        """
        result = get_pair_preference_list()
        return respond( 200, result )
    #End
