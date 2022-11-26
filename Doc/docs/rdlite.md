# RDlite Documentation
RDlite is a light-weight relational database to retrieve data from a local relational database.

## Basic Usage
1. Change the `file_path` variable in `RDlite.__init__` to designate the correct path to the csv files in your local system.
2. Access the "mapping" variable to check the names of the features you intend to retrieve.
3. Retrive the dataframe using the following syntax.
```
agg('company', 'genre', peek=True)
```

## Variables
- Mapping: A `dic[str, str]` that maps a feature to a csv file.
- file_path: The local path to the csv files
- all_features: A list of all available features.

## agg
::: RDlite.accessor.agg
