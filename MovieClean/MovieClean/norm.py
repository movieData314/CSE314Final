import ast
import copy
import pandas as pd
import numpy as np


def append_id(df: pd.DataFrame, ID: int, id_col: str) -> pd.DataFrame:
    """
    append_id
    ---------
    Add a new column named "id" , which has the same value as `ID`, to the given dataframe.

    Note:
        Used as a helper fucntion to easily add ids.

    Arguments:
        df (pd.DataFrame): The dataframe to add ids to
        ID (int): The id for every entry
        id_col (str): The name for the new id column

    Returns:
        pd.DataFrame
            The original dataframe with id added
    """
    df[id_col] = [ID] * df.shape[0]
    return df


def json2df(df: pd.DataFrame, col_name: str, id_col: str) -> pd.DataFrame:
    """
    ## json2df
    Return a new dataframe of data that were stored in json-style strings.

    Extract all json-style data in a dataframe cell and return those data as a single dataframe with another column in the
    original dataframe as the index of the new dataframe

    Arguments:
        df (pd.DataFrame): The dataframe that contains a column \n
            that has json-style strings
        col_name (str): The column that contains json objects
        id_col (str): The column that will be used as the index of \n
            the new dataframe

    Note:
        For large dataframe, this function could be expensive in terms of time and memroy.
        Also watch out for columns with mixed types.

    Returns:
        pd.DataFrame
            The new dataframe made from the data previously \n
            stored in json-format strings
    """
    jsons = df[col_name].apply(ast.literal_eval)
    jsons["id"] = df[id_col]
    dfs = [
        append_id(pd.DataFrame(json), ID, id_col) for json, ID in zip(jsons, df[id_col])
    ]
    return pd.concat(dfs)


def json2series(df: pd.DataFrame, col: str, key: str, id: str) -> pd.Series:
    """
    ## json2series
    Return a new `Series` that contain the interested data previously stored in json-style strings.

    Extract a single key-value pair in the json-style data that are stored in a column into a pd.Series object,
    while ignoring other key-value pairs.

    Arguments:
        df (pd.DataFrame): The dataframe that contains the column of json-style data
        col (str):  The column that contains json-style data
        key (str): The key in the json that maps to the value of interest
        id (str): The name of the column in the original dataframe to be used as the index

    Returns:
        pd.Series
            The Series made from the key-value pair in the jsons

    """
    df = copy.deepcopy(df).set_index(id)
    json_df = df[col].apply(lambda x: ast.literal_eval(x))
    if type(json_df.iloc[0]) != list:
        return json_df.apply(lambda x: x.get(key) if type(x) == dict else None)
    return (
        json_df.apply(lambda x: [each[key] for each in x] if type(x) == list else None)
        .apply(pd.Series)
        .melt(
            ignore_index=False,
            value_name=key,
        )
        .dropna()
        .drop(columns="variable")
        .squeeze()
    )


def split_table(df: pd.DataFrame, key: str, cols: list) -> pd.DataFrame:
    """
    ## split_table
    Return a sub-dataframe of interested data and set a column as index.

    Arguments:
        df (pd.DataFrame): The dataframe that contains the original data
        key (str): The name of the column to use as the index
        cols (list): List of strs that are names of the columns of interest

    Returns:
        pd.DataFrame
            The new sub-dataframe
    """
    return df[cols + [key]].set_index(key)


def id2int(df: pd.DataFrame) -> pd.DataFrame:
    """
    ## id2int
    Convert dtype of the "id" column to int

    Arguments:
        df (pd.DataFrame): The dataframe to do the conversion on

    Returns:
        pd.DataFrame
            The dataframe with index's dtype converted
    """
    temp = df.reset_index()
    temp["id"] = temp["id"].apply(lambda x: int(x) if "-" not in x else None)
    temp = temp.dropna().astype({"id": int})
    return temp.set_index("id")


def cat_encode(data: pd.DataFrame, col_name: str) -> pd.Series:
    """ """
    status = np.array(np.unique(data[col_name]))
    status_code = np.arange(status.shape[0])
    status_map = pd.Series({k: v for k, v in zip(status_code, status)})
    mapping = {v: k for k, v in status_map.items()}
    data.loc[:, col_name] = data[col_name].apply(lambda x: mapping[x])
    return status_map.rename(col_name + "_map")


def drop_duplicate_index(data: pd.DataFrame) -> pd.DataFrame:
    return data[~data.index.duplicated()]
