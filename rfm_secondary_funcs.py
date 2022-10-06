import re
import pandas as pd

def scorer(param, param_name, quantiles):
    """    
    Parameters:
        param      - pd.Series contains RFM metric
        param_name - name of RFM metric  
        quantiles  - dict with R, F and M splits
    Returns:
        Score for passed metric, depending on metric name
        
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
        s        - RFM-score
        segments - pd.DataFrame with split codes and descriptions
    Returns:
        segment description or '000' if R, F or M score don't belong to expected range    
    """
    
    desc = ''        
    
    for split in segments.rfm_split:
        if re.search(split, s):  
            desc = segments[segments.rfm_split == split].description.values[0]    
            
    if desc:
        return desc
    else:
        return '000'
       
        
        