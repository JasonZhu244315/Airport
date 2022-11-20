import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def check_missing_values(df: "DataFrame"):
    """
    Returns a missing value inpection table including both absolute missing number (rows) and percentage, sort by percentage
   
    Parameters
    ----------
    df : DataFrame
    Object to check missing value status.
    """
    
    # Calculate absolute missing number (rows)
    missing_abs = df.isnull().sum().to_frame().reset_index()
    missing_abs.columns = ["Attribute", "Missing#"]
    
    # Calculate missing percentage
    missing_pct = (df.isnull().sum()/len(df)).to_frame().reset_index()
    missing_pct.columns = ["Attribute", "Missing%"]
    
    # Generate and return missing value inspection table
    missing_tbl = missing_abs.merge(missing_pct).sort_values(by = "Missing%", ascending = False).reset_index(drop = True)
    missing_tbl["Missing%"] = round(missing_tbl["Missing%"]  * 100, 2)

    return missing_tbl 



def check_skweness_kurtosis(df: "DataFrame"):
    """
    Returns a skewness & kurtosis inpection table, sort by skewness
   
    Parameters
    ----------
    df : DataFrame
    Object to check skewness & kurtosis status.
    """
    
    # Convert specific attributes to categorical 
    cate_col_ls = [col for col in df.columns if ("_ID" in col) or ("YEAR" in col) or ("QUARTER" in col) or ("ROUNDTRIP" in col) or ("CANCELLED" in col)]
    for cate_col in cate_col_ls:
        df[cate_col] = df[cate_col].astype("object")
    
    # Select numerical attributes
    df_numerical = df.select_dtypes(exclude = "object")
    
    # Calculate skewness
    skewness = df_numerical.skew().to_frame().reset_index()
    skewness.columns = ["Attribute", "Skweness"]

    # Calculate kurtosis
    kurtosis = df_numerical.kurtosis().to_frame().reset_index()
    kurtosis.columns = ["Attribute", "Kurtosis"]

    # Generate and return skewness & kurtosis inspection table
    skeness_kurtosis_tbl = skewness.merge(kurtosis).sort_values(by = "Skweness", ascending = False).reset_index(drop = True)

    return skeness_kurtosis_tbl 



def check_correlation(df: "DataFrame", plot: "bool" = True):
    """
    Returns a correlation table/vizualization for specified DataFrame
   
    Parameters
    ----------
    df : DataFrame
    Object to check correlation.
    plot : bool, default True
    Return correlation vizulization if True, else a correlation table.
    """

    if plot == True:
        plt.figure(figsize = (10, 6))
        mask = np.triu(np.ones_like(df.corr()))
        ax_corr = sns.heatmap(round(df.corr(), 2), annot = True, 
                              cmap = "Greens", mask = mask)
    else:
        return round(df.corr(), 2)