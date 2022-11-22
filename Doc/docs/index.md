# Welcome to The MovieDataset

This project aims to investigate various properties and relations in the context of past movies across languages and countries. There are more than 14 features and tens of thousands of data entries. For our group, we are primarily interested in which genres of movies are the most profitable. 

To help with our analysis, we develop several modules to do cleaning, normalization, and visualization. This documentation is provided to get rid of the fuss and let external clients start their analysis right away.

## Project layout

    docs/
        dashProject/                # The dashboard app to visualize the data in an interactive way
            data_process.py         # Helper functions to convert dataframe to dashboard objects
            tovi_dashboard.py       # The dashboard app
            db_UI.py                # The package of dashboard UI's
        Data/                       # The directory for clean data
            actors.csv
            clean_movie.csv
            collections.csv
            companies.csv
            countries.csv
            genres.csv
            keywords.csv
            languages.csv
            movies_names.csv
            ratings.csv
        Doc/                        # Folder for documentations
            ...
        MovieClean/                 # Installable python module for cleaning and normalizing dataset
            MovieClean/ 
                norm.py
                ...
            ...
        RDlite/                     # A lightweight relational database
            accessor.py
            ...
        314Final_ToviClean.ipynb    # A jupyter notebook to demonstrate the cleaning process
        CSE314ModuleTesting.ipynb   # A jupyter notebook to demonstrate usages of RDlite
        ...                         # Other files

## Installation Instructions

1. Pull the project from this github repository.
    ```
    git pull <url>
    ```

2. Install the MovieClean module
    ```
    pip install -e MovieClean
    ```

3. Configure the data directory in RDlite.__init__
    ```
    file_path = <actual path to the data>
    ```

4. Configure the system path variable in db_UI.py
    ```
    sys.path.append('<local_path>/cse314final')
    ```

After these steps, you should be ready to use the modules within the cse314final folder. 

**Notice** that MovieClean module is the only module with setup.py file, which allows you to use it outside this folder, while the other module are intended to be used within this folder. 

To make non-installable modules accessible by external codes, add this line to the script:
```
import sys
sys.path.append(<pathToModule>)
```

## Examples

### 314Final_ToviClean.ipynb
This notebook shows how we clean the dataset so that they are in long form and could be merged with "df.join" syntax. 

The primary diffculty is that multiple features store giant json format strings or list of json strings in a single cell, which violates the first normal form. Meanwhile, the fact that they are python strings adds to the difficulty of this task because python uses both single quote and double quote to wrap a string adeptively but python's json parser only recognizes double quotes. Therefore, we used a theoretical tool called the abstract syntax tree to reformat the string. 

###  CSE314ModuleTesting
This notebook shows how to do aggregate on dataframes and retrieve the wanted data.

## BDD-style documentation

## Contributing Guide