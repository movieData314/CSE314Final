import pandas as pd
from RDlite.node import Node

# Use Absolute Path
FILE_PATH = "/Users/patricklynch/CSE314Final/Data/"


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



nodes = [Node(FILE_PATH + name, id) for name, id in setup_dict.items()]

all_maps = []
for node in nodes:
    map_local = {feature: node for feature in node.features}
    all_maps.append(map_local)
mapping = {k: v for d in all_maps for k, v in d.items()}

all_features = mapping.keys()
