# movieClean Documentation

## append_id
Add a new column "id" to the give dataframe. Note that every entry will have the same id.
Used as a helper fucntion.

### Parameters
df: pd.DataFrame

- The dataframe to add ids to

ID: int

- The id for every entry

id_col: str

- The name for the new id column

### Returns
pd.DataFrame

- The original dataframe with id added

## json2df

Extract all json-style data in a dataframe cell and return those data as a single dataframe with another column in the
original dataframe as the index of the new dataframe

### Parameters:
df: pd.DataFrame

- The dataframe that contains a column that has json objects

col_name: str
    
- The name of the column that contains json objects

id_col: str
    
- The name of the column that will be used as the index of the new dataframe

### Returns:
pd.DataFrame

- The new dataframe made from the data previously stored in json-format strings

### json2series
Extract a single key-value pair in the json-style data that are stored in a column into a pd.Series object,
while ignoring other key-value pairs.

### Parameters:
df: pd.DataFrame

- The dataframe that contains the column of json-style data

col: str

- The name of the column that contains json-style data

key: str

- The key in the json that maps to the value of interest

id: str

- The name of the column in the original dataframe to be used as the index

### Returns:
pd.Series

- The Series made from the key-value pair in the jsons


## split_table
Return a sub-dataframe of interested data and set a column as index.

### Parameters

df: pd.DataFrame

- The dataframe that contains the original data

key: str

- The name of the column to use as the index

cols: list

- List of strs that are names of the columns of interest

### Returns
pd.DataFrame

- The new sub-dataframe

## id2int
Convert dtype of the "id" column to int

### Parameters
df: pd.DataFrame

- The dataframe to do the conversion on

### Returns
pd.DataFrame

- The dataframe with index's dtype converted