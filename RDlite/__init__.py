import glob

file_path = "/home/themaster/workspace/cse314final/Data/"

import pandas as pd

setup_dict = {
    "companies.csv": ["id"],
    "genres.csv": ["id"],
    "keywords.csv": ["id"],
    "languages.csv": ["id"],
    "ratings.csv": ["id"],
    "countries.csv": ["id"],
    "actors.csv": ["id"],
    "clean_movie.csv": ["id"],
}


class Node:
    path_to_file = None
    id = None
    features = None

    def __init__(self, path: str, id: list):
        peek = pd.read_csv(path, nrows=1)
        self.features = peek.columns.values
        self.path_to_file = path
        self.id = id

    def __leq__(self, other):
        return self.path_to_file < self.path_to_file

    def __getitem__(self, *key):
        return pd.read_csv(self.path_to_file, usecols=[*self.id, *key])

    def peek(self, *key):
        return pd.read_csv(self.path_to_file, usecols=[*self.id, *key], nrows=50)


nodes = [Node(file_path + name, id) for name, id in setup_dict.items()]

all_maps = []
for node in nodes:
    map_local = {feature: node for feature in node.features}
    all_maps.append(map_local)
mapping = {k: v for d in all_maps for k, v in d.items()}

all_features = mapping.keys()
