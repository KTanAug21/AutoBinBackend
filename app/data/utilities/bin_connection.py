import os
from binance import Client
import time

def get_binance_client():
    cli = Client( os.getenv('BIN_API'), os.getenv('BIN_SEC'))
    cli_time = cli.get_server_time()
    cli_time = cli_time['serverTime']
    my_time  = time.time()*1000
    diff = cli_time -my_time
    print( 'C Time {} M Time {} Diff Time: {}'.format(cli_time,my_time, diff ) )
    return cli
#End