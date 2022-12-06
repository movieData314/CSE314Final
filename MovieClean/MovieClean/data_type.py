def cols_to_float(meta_data_df):
    meta_data_df['budget'] = meta_data_df['budget'].astype('float')
    meta_data_df['revenue'] = meta_data_df['revenue'].astype('float')
    
    return meta_data_df