from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api

from app.resources.BinOpenOrderLiveList import BinOpenOrderLiveList
from app.resources.BinOpenOrderDetail import BinOpenOrderDetail
from app.resources.BinOpenOrderList import BinOpenOrderList

from app.resources.PairPreferenceDetail import PairPreferenceDetail
from app.resources.PairPreferenceList import PairPreferenceList 

from app.resources.TestResource import TestResource

from app.resources.UserDetail import UserDetail

from flask_cors import CORS, cross_origin


""" Configuration """ 
load_dotenv()
app  = Flask( __name__ )
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api  = Api( app )


""" Routes / Resources """
api.add_resource( TestResource, "/test-resource" ) 

api.add_resource( BinOpenOrderDetail, "/bin-open-order/detail" ) 
api.add_resource( BinOpenOrderList, "/bin-open-order/list" ) 
api.add_resource( BinOpenOrderLiveList, "/bin-open-order-live/list" ) 

api.add_resource( PairPreferenceDetail, "/pair-preference" ) 
api.add_resource( PairPreferenceList, "/pair-preference/list" ) 

api.add_resource( UserDetail, "/user/detail" ) 



""" Main """ 
if __name__ == "__main__":
    app.run( debug=True ) 