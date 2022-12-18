import requests as r
import pandas as pd
import json

def get_all_movies_2018_plus(api: str) -> dict:
    """
    Get every available movie from TheMovieDB api with a release_date year of 2018 or newer.

    Note:
        Visit https://www.themoviedb.org and create an account to receive an api key (or use mine: c677b8af9185df684a2f9cb664f5159d)

    Note:
        This is time intensive operation. Running it may take a minute to complete. If for whatever reason you believe you need this information cached, consider converting the dictionary to a csv file for storage.

    Arguments:
        api (str): Your personal TheMovieDB api key for querying the api.

    Returns:
        dict
            A dictionary of all the movies released in 2018 to present.

    """
    movies2018plus = []
    for i in range(1, 501):
        req = r.get(
            f"https://api.themoviedb.org/3/movie/top_rated?api_key={api}&language=en-US&page={i}")
        t = req.text
        js = json.loads(t)
        for movie in js['results']:
            if int(movie['release_date'][:4]) > 2017:
                movies2018plus.append(movie)
    return movies2018plus


def get_2018_plus_movie_details(api: str, movies2018plus: dict) -> dict:
    """
    Get revenue, budget, and genre information for movies from TheMovieDB api with a release_date year of 2018 or newer.

    Note:
        Visit https://www.themoviedb.org and create an account to receive an api key (or use mine: c677b8af9185df684a2f9cb664f5159d)
    
    Note:
        This is time intensive operation. Running it may take a couple minutes to complete. If for whatever reason you believe you need this information cached, consider converting the dictionary to a csv file for storage.

    Arguments:
        api (str): Your personal TheMovieDB api key for querying the api.

        movies2018plus (dict): A dictionary of all the movies released in 2018 to present.

    Returns:
        dict
            A dictionary including the revenue, budget, and genres of of all the movies released in 2018 to present.
    """
    details_movies2018plus = []
    for movie in movies2018plus:
        req = r.get(
            f"https://api.themoviedb.org/3/movie/{movie['id']}?api_key={api}&language=en-US")
        t = req.text
        js = json.loads(t)
        genres = [g['name'] for g in js['genres']]
        details_movies2018plus.append([js['revenue'], js['budget'], genres])
    return details_movies2018plus


def movie_details_to_df(details_movies2018plus: dict) -> pd.DataFrame:

    """
    Convert a dictionary containing revenue, budget, and genre information to a dataframe.

    Arguments:
        details_movies2018plus (dict): A dictionary including the revenue, budget, and genres of of all the movies released in 2018 to present.

    Returns:
        pd.DataFrame
            A dataframe including the revenue, budget, and genres of of all the movies released in 2018 to present.
    """
    apiDF = pd.DataFrame(details_movies2018plus,
                     columns=['revenue', 'budget', 'genres'])
    return apiDF
