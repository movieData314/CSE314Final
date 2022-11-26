from RDlite import mapping, file_path
import pandas as pd


def agg(*features, peek=False) -> pd.DataFrame:
    """
    Return a dataframe containing the features of interest.

    Arguments:
        features (strs): Names of the features to retrieve
        peek (bool): A boolean default to False. \n
            If true, it returns the first 50 entries from each feature.

    Returns:
        pd.DataFrame
            A dataframe that contains the features of interest
    """
    result = None
    filez = list(set([mapping[x] for x in features]))
    for each in filez:
        if each in ["actors.csv", "movies_names.csv"]:
            continue
        to_join = (
            pd.read_csv(file_path + each, nrows=50)
            if peek
            else pd.read_csv(file_path + each)
        )
        if result is None:
            result = to_join
        else:
            if "id" in result.columns:
                result = result.set_index("id").join(to_join.set_index("id"))
            else:
                result = result.join(to_join.set_index("id"))
    if each in ["actors.csv", "movies_names.csv"]:
        other = (
            pd.read_csv(file_path + "actors.csv", nrows=50)
            if peek
            else pd.read_csv(file_path + "actors.csv", nrows=50)
        )
        to_join = (
            pd.read_csv(file_path + "movies_names.csv", nrows=50)
            if peek
            else pd.read_csv(file_path + "movies_names.csv", nrows=50)
        )
        to_join = to_join.join(other.set_index("name"), on="name")
        result.join(to_join.set_index("id"))
    return result
