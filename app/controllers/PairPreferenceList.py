
""" PairPreferenceList """
from app.data.PairPreferenceList import get_db_list
def get_pair_preference_list():
    """
    resource: PairPreferenceList.get
    """ 
    return get_db_list()
#End 

from app.data.utilities.formatter import ext_attr_from_dict_as_list
def sup_pair_name_list():
    """
    Supplimentary function to get_pair_preference_list
    Returnas a list containing unique pairs from dictionary result of get_pair_preference_list
    """

    pair_preference_dict = get_pair_preference_list()
    return ext_attr_from_dict_as_list( pair_preference_dict, 'pair', True )
#End
