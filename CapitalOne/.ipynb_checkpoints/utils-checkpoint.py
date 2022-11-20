import pyforest
import string, re

def check_str_punc(value):
    """
    Returns a True for values containing string or punctuations (except for .), False for float number only
   
    Parameters
    ----------
    value : 
    Object to check if it's a float.
    """
    
    punctuation = string.punctuation.replace(".", "")
    str_punc_num = 0
    
    for i in value:
        if (i.isalpha()) | (i in punctuation):
            str_punc_num += 1
        else:
            str_punc_num += 0

    if str_punc_num > 0:
        return True
    else:
        return False