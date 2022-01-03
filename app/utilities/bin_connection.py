import os
from binance import Client

def get_binance_client():
    return Client( os.getenv('BIN_API'), os.getenv('BIN_SEC') )
#End