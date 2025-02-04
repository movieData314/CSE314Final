# Welcome to The MovieDataset

This project aims to investigate various properties and relations in the context of past movies across languages and countries. There are more than 14 features and tens of thousands of data entries. For our group, we are primarily interested in which genres of movies are the most profitable. 

To help with our analysis, we develop several modules to do cleaning, normalization, and visualization. This documentation is provided to get rid of the fuss and let external clients start their analysis right away.

## Project layout

    CSE314FINAL/
        API/
            API/                    # API module to access new movie data from imbd
                get_api_data.py
            setup.py
        dashProject/                # The dashboard app to visualize the data in an interactive way
            dashProject/
                data_process.py     # Helper functions to convert dataframe to dashboard objects
                tovi_dashboard.py   # The dashboard app
                db_UI.py            # The package of dashboard UI's
            setup.py
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
            docs/
                api.md
                dashpro.md
                index.md
                movieClean.md
                normalization.md
                rdlite.md
            site/                   # Documentation website source code
                ...
        MovieClean/                 # Python module for cleaning and normalizing dataset
            MovieClean/
                data_type.py
                genre_cleaning.py 
                norm.py
                ...
            setup.py
        Normalization/              # Normalization package for genre
            Normalization/
                normalize_genre.py 
            setup.py
        RDlite/                     # A lightweight relational database for dashboard
            RDlite/
                accessor.py
            setup.py

        API_Example.ipynb    # A jupyter notebook to demonstrate the API process
        Cleaning_Example.ipynb    # A jupyter notebook to demonstrate the cleaning process
        env.yml
        Genre_Example.ipynb    # A jupyter notebook to demonstrate the genre analysis process
        ModuleTesting.ipynb   # A jupyter notebook to demonstrate usages of RDlite
        profit.ipynb   # A jupyter notebook to demonstrate visualize and perform profit analysis

## Installation Instructions

1. Pull the project from this github repo: https://github.com/movieData314/CSE314Final 

    ```
    git pull https://github.com/movieData314/CSE314Final 
    ``` 

2. Create conda environment from the included yml file

    ```
    conda env create -f env.yml
    ```

3. Activate conda environments 

    ```
    conda activate general
    ```

4. Install the modules 

    ```
    pip install -e MovieClean
    pip install -e API
    ...
    ```

5. <Optional> Configure the RDlite module to aggregate clean data. (Work on clean data only) 

    ```
    FILE_PATH = <absolute path to the data>
    ``` 

6. Configure the system path variable in db_UI.py 

    ```
    sys.path.append('<local_path>/cse314final')
    ```

After these steps, you should be ready to use the modules within the cse314final folder. 

**Notice** that all of the modules are written in a way that they can be install using pip

Tip to load local package withou installing
```
import sys
sys.path.append(<pathToModule>)
```

## Getting Started Guide
With all the modules installed and set up, you are ready to start your own analysis using the movie data. For correlation analysis or ml model building we provide the following guide to get you prepared.

1. Clean the data with MovieClean: extract json-style strings, fix dtypes and set index columns with tools provided in the module.

2. Normalize the data: make separate tables with different gradularity to optimize space usages and make the data easy to work with using `Normalization` module.

3. Add more data: The provided dataset contains movies prior to 2018. To add more recent movie information, use `API` module to retrieve the data from MovieDB.

4. Quick visualization: Before writing any code, use `dashProject` module to navigate through the sample data and visualize correlation and central tendency.

5. Visit the examplery notebooks for ideas or hint to use our modules.

## Examples

### Cleaning_Example.ipynb
This notebook shows how we clean the dataset so that they are in long form and could be merged with "df.join" syntax. 

The primary diffculty is that multiple features store giant json format strings or list of json strings in a single cell, which violates the first normal form. Meanwhile, the fact that they are python strings adds to the difficulty of this task because python uses both single quote and double quote to wrap a string adeptively but python's json parser only recognizes double quotes. Therefore, we used a theoretical tool called the abstract syntax tree to reformat the string. 

###  ModuleTesting
This notebook shows how to do aggregate on dataframes and retrieve the wanted data.

### API_Example
This notebook shows examples of retrieving more movie data entries as complement to the existing ones.

### Genre_Example
This notebook shows how we normalize the genre feature for our analysis.

### profit
This notebook shows the workflow how we find the most profitable movie genre.

## BDD-style documentation

**Title: Data Cleaning**

**As a** Data Anlyst who just obtained the raw movie data <br />
**I want**  to clean the raw data <br />
**So that** the data contains no errors and no duplicates and makes sense for real movies <br />

**Scenario** 1: The data should not have complex data structure. <br />
**Given** a dataset that has feature columns (like genre) with json encoded as single strings <br />
**When** we try to parse these columns <br />
**Then** the key-value pairs are decoded into a dataframe or series <br />

**Scenario** 2: The numerals in the data should have plausible movie feature values <br />
**Given** a column that represents real values (like budget) but contains many 0’s <br />
**When** we clean this column <br />
**Then** 0’s are replaced by not-a-number flag <br />

**Scenario** 3: The data should not have movie duplicates <br />
**Given** a dataset that contains exactly the same two rows <br />
**When** we clean this data <br />
**Then** duplicate rows (movies) are removed and the index is unique <br />

**Title**: Data Normalization <br />

**As a** data analyst who has cleaned the movie data <br />
**I want** rescale the dataset and split it up to form separate files with different granularity <br />
**So that** each file is optimized in size and properly indexed <br />

**Scenario** 1: The index column in files should have the same dtypes <br />
**Given** two dataframes with the “id” column as the index but one column has strings rather than integers, <br />
**When** we normalize the data, <br />
**Then** all the index columns for the movies contain integers <br />

**Scenario** 2: Each data entry should have unique index<br />
**Given** a dataframe of movie characters which cannot be identified by movie-id alone,<br />
**When** we normalize the data,<br />
**Then** both movie-id and the name of actor are used as index<br />

**Scenario** 3: Data with its own granularity should be split into a new table,<br />
**Given** a dataframe of actors that is a many-to-many relationship to movie-id<br />
**When** normalize the data,<br />
**Then** a junction table for actors and movie-id is separated from rest of the movie data<br />

**Title**: Aggregation<br />

**As a** data analyst who wants to explore the movie data<br />
**I want** to aggregate the tables containing the data we want,<br />
**So that**: I can calculate correlation and visualize the movie data<br />

**Scenario** 1: Separate tables should be able to be joined together using keys and foreign keys<br />
**Given** a one-to-many table of genre data and a one-to-one movie info table,<br />
**When** we merge the tables together,<br />
**Then** the two tables are joined together based the movie-id column<br />


**Title**: Dashboard<br />

**As a** data analyst who obtained the movie data for the first time,<br />
**I want** to do some quick exploration on the data<br />
**So that** I have a sense of data about its structure, data types and other aspects<br />

**Scenario** 1: The dashboard app should provides some samples of the movie data <br />
**When** we want to look at the data itself,<br />
**Then** the dashboard samples a small chunk of data from each table present the joined table to the user<br />
**Then** the user can navigate through the data using scroll bars and buttons<br />

**Scenario** 2: The dashboard app should visualize selected data <br />
**Given** all the clean data,<br />
**When** the user selectes two features (budget, revenue, etc.) from the data,<br />
**Then** the app decides between a scatter plot or a bar plot to draw based on the data types<br />
**Then** the app present a plot that allows the user to zoom in with cursor<br />

**Scenario** 3: The dashboard app should calculate the correlation<br />
**Given** two numerical features (budget, revenue, etc.) selected by the user,<br />
**When** the user hits the “submit” button,<br />
**Then** the app presents a table including information such as quartiles and correlations<br />

**Title**: API
**As a** movie lover 
**I want** to gather information about recent movies
**So that** the movie dataset is more complete

**Scenario** 1: The TheMovieDB api shoud return movies released after 2017
**When** we request the movies for TheMovieDB api,
**Then** the api returns a dataframe of the movie's details

## Contributing Guide

Project made by Yan Zhou, Patrick Lynch, Won Young Kang, Tovi Tu

First, thanks for for considering contributing to our project! There are many ways you can help out.

1. Reporting a bug
2. Submitting a fix
3. Proposing new features

### Report a bug

If you spot a problem with the docs, report the issue by opening a new [issue](https://github.com/movieData314/CSE314Final). 

### Make Changes

We Use Github [Flow](https://docs.github.com/en/get-started/quickstart/github-flow), So All Code Changes Happen Through Pull Requests.

When your code is ready to be submitted, [submit a pull request](https://github.com/movieData314/CSE314Final/pulls) to begin the code review process.

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Issue that pull request!

### License
By contributing, you agree that your contributions will be licensed under its WUSTL License.


### Reference
This document was adapted from the open-source contribution guidelines [here](https://gist.github.com/briandk/CONTRIBUTING.md) and also from yahoo [here](https://yahoo.github.io/oss-guide/docs/publishing/publishing-template/Contributing.html)




