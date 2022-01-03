from flask_restful import Resource

from app.utilities.response import respond
from app.controllers.PairPreferenceDetail import delete_detail, get_detail, patch_pair_preference, put_pair_preference

class PairPreferenceDetail( Resource ):
    
    def delete( self ):
        """
        Delete details of the pair preference requested through id
        """
        data = delete_detail()
        return respond( 200, data )
    #End

    def get( self ): 
        """
        Retrieve details of the pair preference requested through id
        """
        result = get_detail()
        return respond( 200, result )
    #End

    def put( self ):
        """
        Create details of a new pair preference
        """
        result = put_pair_preference()
        return respond( 200, result )
    #End

    def patch( self ):
        """
        Create details of a new pair preference
        """
        result = patch_pair_preference()
        return respond( 200, result )
    #End

#End

