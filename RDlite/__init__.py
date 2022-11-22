import glob

mapping = {
    "company": "companies.csv",
    "collection": "collections.csv",
    "genre": "genres.csv",
    "keyword": "keywords.csv",
    "rating": "ratings.csv",
    "language": "languages.csv",
    "country": "countries.csv",
    "name": "movies_names.csv",
    "character": "actors.csv",
    "gender": "actors.csv",
    "movie": "clean_movie.csv",
    "adult": "clean_movie.csv",
    "budget": "clean_movie.csv",
    "original_language": "clean_movie.csv",
    "original_title": "clean_movie.csv",
    "overview": "clean_movie.csv",
    "popularity": "clean_movie.csv",
    "release_date": "clean_movie.csv",
    "revenue": "clean_movie.csv",
    "runtime": "clean_movie.csv",
    "status": "clean_movie.csv",
    "video": "clean_movie.csv",
    "vote_average": "clean_movie.csv",
    "vote_count": "clean_movie.csv",
}

file_path = "/home/themaster/workspace/cse314final/Data/"

all_features = list(mapping.keys())
