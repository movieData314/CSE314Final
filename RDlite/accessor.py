from RDlite import mapping, file_path
import pandas as pd
import numpy as np


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
    access_nodes = [mapping[each] for each in features]
    for node, feature in zip(access_nodes, features):
        if result is None:
            result = (node[feature] if not peek else node.peek(feature)).set_index(node.id)
        else:
            result = result.join((node[feature] if not peek else node.peek(feature)).set_index(node.id), on=node.id)
    return result
        