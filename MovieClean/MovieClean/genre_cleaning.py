import json
import pandas as pd


def return_names_list(dic: dict) -> list[str]:
    '''
    ## return_names_list
    
    Returns a list of string that contains the genres of the movie

    Arguments:
        dic (dict): a genre dictionary derived from the JSON formatted column of the metadata dataset
        
    Returns:
        list[str]
            a list of string that contains the genres of the movie
    '''
    genre_list = []
    try:
        for key in dic:
            val = key['name']
            genre_list.append(val)
    except:
        return genre_list
  
    return genre_list

def extract_genre(meta_data_df: pd.DataFrame) -> pd.DataFrame:
    '''
    ## extract_genre
    
    Returns a list of string that contains the genres of the movie

    Arguments:
        meta_data_df (pd.DataFrame): The dataframe that contains the original movie meta data
        
    Returns:
        pd.DataFrame
            a meta data dataframe with a column named genre_names_list, which contains a list of genres, added to it
    '''
    meta_data_df['genre_names'] = meta_data_df['genres'].apply(lambda x: [json.loads(idx.replace("'", '"')) for idx in [x]][0])
    meta_data_df['genre_names_list'] = meta_data_df['genre_names'].apply(lambda dic: return_names_list(dic))
    meta_data_df.drop(columns=['genres', 'genre_names'], inplace=True)

    return meta_data_df