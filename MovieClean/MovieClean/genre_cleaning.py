import json
import pandas as pd


def return_names_list(dic: dict) -> list[str]:
    '''
    description:
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
    description:
    '''
    meta_data_df['genre_names'] = meta_data_df['genres'].apply(lambda x: [json.loads(idx.replace("'", '"')) for idx in [x]][0])
    meta_data_df['genre_names_list'] = meta_data_df['genre_names'].apply(lambda dic: return_names_list(dic))
    meta_data_df.drop(columns=['genres', 'genre_names'], inplace=True)

    return meta_data_df