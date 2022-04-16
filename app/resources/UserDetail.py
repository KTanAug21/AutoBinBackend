from flask_restful import Resource
from app.data.utilities.response import respond
from app.controllers.UserDetail import put_user_detail, get_user_detail
from decorator import login_required

class UserDetail( Resource ):

    @login_required
    def put( self ):
        """ 
        Add details as a row in collection
        """
       
        result = put_user_detail()
        return respond( 200, result )
    #End

    @login_required
    def get( self ):
        """
        Get User details:
            if token:
                user id, name, email

        """
        result = get_user_detail()
        return respond( 200, result )
    #End
