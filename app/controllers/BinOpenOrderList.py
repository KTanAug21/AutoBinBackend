from app.controllers.BinOpenOrderLiveList import get_list as get_live_list
from app.controllers.PairPreferenceList import get_pair_preference_list
from app.data.BinOpenOrderList import get_db_list
from app.data.BinOpenOrderDetail import upsert_item
from app.data.PairPreferenceList import update_sync_db_list as update_pair_sync_list
from app.data.utilities.date_time import current_ms_time, time_is_older_than
import datetime

""" BinOpenrOrderList """

def get_list():
    """
    resource: BinOpenOrderList.get
    Get list of open orders that where retrieved within the last one hour from live binance api data

    Check if there is any pair preference that was not synced within the last hour
    If there is, this is an indicator that a sync from binance is necessary
    so sync it
    
    Then return records from db list

    """
    # Get pair list
    pair_list = get_pair_preference_list()
    
    # Check if there are pairs that need syncing
    sync = False
    for pair in pair_list:
       
        if 'synced_at' not in pair or pair['synced_at'] is None:
            sync = True
        elif time_is_older_than( int(pair['synced_at']), 1 ):
            # Previous sync is older than one hour, need to resync again
            sync = True
        
        if sync:
            break
    #End 

    # Existing records in db for reference
  
    db_list = get_db_list()
    if sync:
    
        # Get from live data
        print( 'Syncing...' )
        live_list = get_live_list()

        # Add new records to db
        for order in live_list:
            
            if order['status'] == 'NEW':
            
                print( 'Upserting order to db {}'.format(order) )
                upsert_item( {'orderId':order['orderId']}, order )
                order['synced_at'] = current_ms_time()
            
            """elif order['status'] == 'FILLED':

                # Get record details
                record = get_record_details_from_get_db_list( order['orderId'] )

                # Check if reverse order available
                if check_if_record_has_reverse_order( record ): 
                    
                    # Trigger reverse order
                    make_reverse_order( record )
            """
        # Get records from db

        #update_pair_sync_list()
        db_list = get_db_list()

    else:
        print( 'Not syncing' )
        
    
    return db_list
    
#End 
