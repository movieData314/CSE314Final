import glob

# mapping = {
#     "company": "companies.csv",
#     "collection": "collections.csv",
#     "genre": "genres.csv",
#     "keyword": "keywords.csv",
#     "rating": "ratings.csv",
#     "language": "languages.csv",
#     "country": "countries.csv",
#     "name": "movies_names.csv",
#     "character": "actors.csv",
#     "gender": "actors.csv",
#     "movie": "clean_movie.csv",
#     "adult": "clean_movie.csv",
#     "budget": "clean_movie.csv",
#     "original_language": "clean_movie.csv",
#     "original_title": "clean_movie.csv",
#     "overview": "clean_movie.csv",
#     "popularity": "clean_movie.csv",
#     "release_date": "clean_movie.csv",
#     "revenue": "clean_movie.csv",
#     "runtime": "clean_movie.csv",
#     "status": "clean_movie.csv",
#     "video": "clean_movie.csv",
#     "vote_average": "clean_movie.csv",
#     "vote_count": "clean_movie.csv",
# }

# file_path = "/home/themaster/workspace/cse314final/Data/"

# all_features = list(mapping.keys())

import pandas as pd


class Node:
    path_to_file = None
    id = None
    features = None

    def __init__(self, path, id):
        peek = pd.read_csv(path, nrows=1)
        features = peek.columns.values
        self.path_to_file = path
        self.id = id

    def __getitem__(self, *key):
        return pd.read_csv(self.path_to_file)[[id, *key]].set_index(id)
