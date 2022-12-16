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

**Title: Data Cleaning**

**As a** Data Anlyst who just obtained the raw movie data <br />
**I want**  to clean the raw data <br />
**So that** the data contains no error and no duplicates and makes sense in the real-life context <br />

**Scenario** 1: The data should not have complex data structure. <br />
**Given** a dataset that has columns with json encoded as single strings <br />
**When** we try to parse these columns <br />
**Then** the key-value pairs are decoded into a dataframe or series <br />

**Scenario** 2: The numerals in the data should have plausible values <br />
**Given** a column that represent mony but contains many 0’s <br />
**When** we clean this column <br />
**Then** 0’s are replaced by not-a-number flag <br />

**Scenario** 3: The data should not have duplicates <br />
**Given** a dataset that contains exactly the same two rows <br />
**When** we clean this data <br />
**Then** duplicate rows are removed and the index is unique <br />

**Title**: Data Normalization <br />

**As a** data analyst who have cleaned the data <br />
**I want** rescale the dataset and split it up to form separate files with different gradularity <br />
**So that** each file is optimized in size and properly indexed <br />

**Scenario** 1: The index column in files should have the same dtypes <br />
**Given** two dataframes with the “id” column as the index but one column has strings rather than integers, <br />
**When** normalize the data, <br />
**Then** all index columns contains integers <br />




**Scenario** 2: Each data entry should have unique index<br />
**Given** a dataframe of movie characters which cannot be identified by movie-id alone,<br />
**When** we nromalize the data,<br />
**Then** both movie-id and the name of actor are used as index<br />

**Scenario** 3: Data with its own granularity should be split into a new table,<br />
**Given** a dataframe of actors that a many-to-many relationship to movie-id<br />
**When** normalize the data,<br />
**Then** a junction table for actors and movie-id is separated from rest of the movie data<br />

**Title**: Aggregation<br />

**As a** data analyst who wants to explore the data of interest<br />
**I want** to aggregate the tables containing the data we want,<br />
**So that**: I can calculate correlation and visualize those data<br />

**Scenario** 1: Separate tables should be able to be joined together using keys and foreign keys<br />
**Given** a one-to-many table of genre data and a one-to-one movie info table,<br />
**When** we merge the tables together,<br />
**Then** the two tables are joined together based the movie-id column<br />


**Title**: Dashboard<br />

**As a** data analyst who obtain the data for the first time,<br />
**I want** to do some quick exploration on the data<br />
**So that** I have a sense of data about its structure, data types and other aspects<br />

**Scenario** 1: The dashboard app should provides some samples of the data <br />
**When** we want to look at the data itself,<br />
**Then** the dashboard samples a small chunk of data from each table present the joined table to the user<br />
**Then** the user can navigate through the data using scroll bars and buttons<br />

**Scenario** 2: The dashboard app should visualize selected data <br />
**Given** all the clean data,<br />
**When** the user selectes two features from the data,<br />
**Then** the app decides between a scatter plot or a bar plot to draw based on the data types<br />
**Then** the app present a plot that allows the user to zoom in with cursor<br />

**Scenario** 3: The dashboard app should calculate the correlation<br />
**Given** two numerical features selected by the user,<br />
**When** the user hit the “submit” button,<br />
**Then** the app presents a table including information such as quartiles and correlations<br />
