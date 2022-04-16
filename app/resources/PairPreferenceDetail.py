from flask_restful import Resource

from app.data.utilities.response import respond
from app.controllers.PairPreferenceDetail import delete_detail, get_detail, patch_pair_preference, put_pair_preference
from decorator import login_required

class PairPreferenceDetail( Resource ):
    
    @login_required
    def delete( self ):
        """
        Delete details of the pair preference requested through id
        """
        data = delete_detail()
        return respond( 200, data )
    #End

    @login_required
    def get( self ): 
        """
        Retrieve details of the pair preference requested through id
        """
        result = get_detail()
        return respond( 200, result )
    #End

    @login_required
    def put( self ):
        """
        Create details of a new pair preference
        """
        result = put_pair_preference()
        return respond( 200, result )
    #End

    @login_required
    def patch( self ):
        """
        Create details of a new pair preference
        """
        result = patch_pair_preference()
        return respond( 200, result )
    #End

#End

