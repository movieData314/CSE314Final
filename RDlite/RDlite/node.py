import pandas as pd
class Node:
    """
    The Node class serves as the proxy between the data saved locally 
    and the programs intend to use them. Each physical file is aliased 
    by a Node object.

    Data Fields:
        path_to_file (str): The local directory to the file.
        id (str): The index column of this specific file.
        features: The features stored.
    
    Attributes:
        []operator: Return the selected data in a pandas dataframe
        peek: Return the first 50 rows of the selected data
    """
    path_to_file = None
    id = None
    features = None

    def __init__(self, path: str, id: list):
        peek = pd.read_csv(path, nrows=1)
        self.features = peek.columns.values
        self.path_to_file = path
        self.id = id

    def __leq__(self, other):
        return self.path_to_file < other.path_to_file

    def __getitem__(self, *key):
        return pd.read_csv(self.path_to_file, usecols=[*self.id, *key])

    def peek(self, *key) -> pd.DataFrame:
        """
        Return the first 50 rows of selected data.

        Arguments:
            key (strs): Features of interest in this specifc file

        Returns:
            pd.DataFrame
                A dataframe contain the selected features plus the index column
        """
        return pd.read_csv(self.path_to_file, usecols=[*self.id, *key], nrows=50)
