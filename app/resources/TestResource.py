from flask_restful import Resource
from app.data.utilities.bin_connection import get_binance_client
from app.data.utilities.response import respond

class TestResource( Resource ):

    def get( self ):
        cli = get_binance_client()
        return respond( 200, {} )
    #End