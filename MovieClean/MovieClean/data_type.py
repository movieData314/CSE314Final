import pandas as pd

def budget_revenue_cols_to_float(meta_data_df: pd.DataFrame) -> pd.DataFrame:
    '''
    ## budget_revenue_cols_to_float
    
    Returns a dataframe with data type of its columns correctly assigned

    Arguments:
        meta_data_df (pd.DataFrame): The dataframe that contains the original movie meta data
        
    Returns:
        pd.DataFrame
            a meta data dataframe with correct data types
    '''
    meta_data_df = meta_data_df[~(meta_data_df['id'].str.contains('-'))]
    meta_data_df['id'] = meta_data_df['id'].astype(float)
    meta_data_df['budget'] = meta_data_df['budget'].astype('float')
    meta_data_df['revenue'] = meta_data_df['revenue'].astype('float')
    rev_budget_filter = ((meta_data_df['revenue'] > 0 ) & (meta_data_df['revenue'].notna()) & (meta_data_df['budget'] > 0 ) & (meta_data_df['budget'].notna()))
    meta_data_df = meta_data_df[rev_budget_filter]
    return meta_data_df