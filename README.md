# CSE314Final

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

Click github-pages then view deployment or visit https://moviedata314.github.io/CSE314Final/ to view the documentation website.
