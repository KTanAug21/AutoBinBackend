import time
import datetime

def current_ms_time():
    return round(time.time() * 1000)
#End

def time_is_older_than( time, hours ):
    """
    Determine whether a time (ms) is older than a specific number of hours
    
    Args:
        time - time to check
        hours - number of hours

    Return:
        ( Boolean )
    """
   
   
    # Convert ms time to datetime
    time_converted = datetime.datetime.fromtimestamp(time/1000.0)
    
    # Convert hours being compared to to seconds
    hour_in_seconds = hours * 3600

    if time_converted < datetime.datetime.utcnow()-datetime.timedelta(seconds=hour_in_seconds):
        return True
    else:
        return False
#End