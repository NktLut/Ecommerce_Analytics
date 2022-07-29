import re
import pandas as pd

def scorer(param, param_name, quantiles):
    """    
    Parameters:
        param      - pd.Series element
        param_name - name of pd.Series
        quantiles  - dict with R, F and M splits
    Returns:
        Resulting score for passed param, depending on param_name
        
    """
    
    if param_name == 'Recency':
        if param <= quantiles[param_name][.2]:
            return '5'
        elif param <= quantiles[param_name][.4]:
            return '4'
        elif param <= quantiles[param_name][.6]:
            return '3'
        elif param <= quantiles[param_name][.8]:
            return '2'
        else:
            return '1'
    else:
        if param <= quantiles[param_name][.2]:
            return '1'
        elif param <= quantiles[param_name][.4]:
            return '2'
        elif param <= quantiles[param_name][.6]:
            return '3'
        elif param <= quantiles[param_name][.8]:
            return '4'
        else:
            return '5' 
            

def segmenter(s, segments):
    """
    Parameters:
        s        - element from rfm_score pd.Series
        segments - pd.DataFrame with split codes and description
    Returns:
        segment description or '000' if r, f or m score don't belong to expected range    
    """
    
    desc = ''        
    
    for split in segments.rfm_split:
        if re.search(split, s):  
            desc = segments[segments.rfm_split == split].description.values[0]    
            
    if desc:
        return desc
    else:
        return '000'
       
        
        