import time
import datetime

def current_ms_time():
    """
    Get current time in milliseconds

    Args:
        None
    Return:
        Integer - time in milliseconds of calculated date
    """
    return round(time.time() * 1000)
#End


def several_days_from_date_in_ms_time( date_in_ms, number_of_days ):
    """
    Get a specific day, <number_of_days> from current time in milliseconds
    
    Args:
        date_in_ms     - (int) Date in ms
        number_of_days - (int) Number of days to increment from today

    Return:
        Integer - time in milliseconds of calculated date
    """
    milliseconds_to_add = number_of_days * 24 * 60 * 60 * 1000
    return date_in_ms + milliseconds_to_add
#End


def time_is_older_than( time, hours ):
    """
    Determine whether a time (ms) is older than a specific number of hours
    
    Args:
        time - time to check
        hours - number of hours

    Return:
        Boolean
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