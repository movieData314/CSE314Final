import pandas as pd

def one_hot_encoding(meta_data_df: pd.DataFrame) -> pd.DataFrame:
    '''
    ## one_hot_encoding
    
    Returns a dataframe with columns for each genre that are created with one-hot encoding
    
    Arguments:
        meta_data_df (pd.DataFrame): The dataframe that contains the original movie meta data
        
    Returns:
        pd.DataFrame
            a dataframe with columns for each genre that are created with one-hot encoding
    '''

    meta_data_genre_col = meta_data_df['genre_names_list']
    genres_onehot = pd.get_dummies(meta_data_genre_col.apply(pd.Series).stack(), prefix='Genre').sum(level=0)
    meta_data_genre_df = meta_data_df.join(genres_onehot)

    return meta_data_genre_df

def movie_profit_calculation(meta_data_df: pd.DataFrame) -> pd.DataFrame:
    '''
    ## movie_profit_calculation
    
    Caluculates profit for each movie and returns a dataframe with a profit column added
    
    Arguments:
        meta_data_df (pd.DataFrame): The dataframe that contains the original movie meta data
        
    Returns:
        pd.DataFrame
            a dataframe with a profit column added
    '''

    meta_data_df['profit'] = meta_data_df['revenue'] - meta_data_df['budget']
    
    return meta_data_df

def movie_revenue_budget_ratio(meta_data_df: pd.DataFrame) -> pd.DataFrame:
    '''
    ## movie_revenue_budget_ratio
    
    Caluculates a revenue-budget ratio of each movie and returns a dataframe with a revenue-budget ratio column added
    
    Arguments:
        meta_data_df (pd.DataFrame): The dataframe that contains the original movie meta data
        
    Returns:
        pd.DataFrame
            a dataframe with a revenue-budget ratio column added
    '''

    meta_data_df['ratio_rev_budget'] = meta_data_df['revenue'] / meta_data_df['budget']
    
    return meta_data_df

def genre_median_statistics(meta_data_df: pd.DataFrame) -> pd.DataFrame:
    '''
    ## genre_median_statistics
    
    Caluculates median statistics for each genre and returns a dataframe with a those statistics
    
    Arguments:
        meta_data_df (pd.DataFrame): The dataframe that contains the original movie meta data
        
    Returns:
        pd.DataFrame
            a dataframe with a median statistics of each genre
    '''

    genre_list = ['Genre_Action', 'Genre_Adventure', 'Genre_Animation', 'Genre_Comedy', 'Genre_Crime', 'Genre_Documentary', 'Genre_Drama', 'Genre_Family', 'Genre_Fantasy', 'Genre_Foreign', 'Genre_History', 'Genre_Horror', 'Genre_Music', 'Genre_Mystery', 'Genre_Romance', 'Genre_Science Fiction', 'Genre_TV Movie', 'Genre_Thriller', 'Genre_War', 'Genre_Western']
  
    revenue_median = []
    budget_median = []
    profit_median = []
    ratio_median = []

    for genre in genre_list:
        genre_revenue_median = meta_data_df[meta_data_df[genre] == 1.0]['revenue'].median()
        revenue_median.append(genre_revenue_median)
        genre_budget_median = meta_data_df[meta_data_df[genre] == 1.0]['budget'].median()
        budget_median.append(genre_budget_median)
        genre_profit_median = meta_data_df[meta_data_df[genre] == 1.0]['profit'].median()
        profit_median.append(genre_profit_median)
        genre_ratio_median = meta_data_df[meta_data_df[genre] == 1.0]['ratio_rev_budget'].median()
        ratio_median.append(genre_ratio_median)

    genre_median_df = pd.DataFrame(
    {
        'revenue': revenue_median,
        'budget': budget_median,
        'profit': profit_median,
        'rev/budget': ratio_median
    }, 
    index=genre_list)
  
    return genre_median_df

def genre_mean_statistics(meta_data_df: pd.DataFrame) -> pd.DataFrame:
    '''
    ## genre_mean_statistics
    
    Caluculates mean statistics for each genre and returns a dataframe with a those statistics
    
    Arguments:
        meta_data_df (pd.DataFrame): The dataframe that contains the original movie meta data
        
    Returns:
        pd.DataFrame
            a dataframe with a mean statistics of each genre
    '''
    genre_list = ['Genre_Action', 'Genre_Adventure', 'Genre_Animation', 'Genre_Comedy', 'Genre_Crime', 'Genre_Documentary', 'Genre_Drama', 'Genre_Family', 'Genre_Fantasy', 'Genre_Foreign', 'Genre_History', 'Genre_Horror', 'Genre_Music', 'Genre_Mystery', 'Genre_Romance', 'Genre_Science Fiction', 'Genre_TV Movie', 'Genre_Thriller', 'Genre_War', 'Genre_Western']
  
    revenue_mean = []
    budget_mean = []
    profit_mean = []
    ratio_mean = []

    for genre in genre_list:
        genre_revenue_mean = meta_data_df[meta_data_df[genre] == 1.0]['revenue'].mean()
        revenue_mean.append(genre_revenue_mean)
        genre_budget_mean = meta_data_df[meta_data_df[genre] == 1.0]['budget'].mean()
        budget_mean.append(genre_budget_mean)
        genre_profit_mean = meta_data_df[meta_data_df[genre] == 1.0]['profit'].mean()
        profit_mean.append(genre_profit_mean)
        genre_ratio_mean = meta_data_df[meta_data_df[genre] == 1.0]['ratio_rev_budget'].mean()
        ratio_mean.append(genre_ratio_mean)

    genre_mean_df = pd.DataFrame(
    {
        'revenue': revenue_mean,
        'budget': budget_mean,
        'profit': profit_mean,
        'rev/budget': ratio_mean
    }, 
    index=genre_list)
  
    return genre_mean_df