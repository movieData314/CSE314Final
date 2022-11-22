# RDlite Documentation

## Agg
Return a dataframe containing the features of interest
### Parameters
**features**: strs (variable size)

names of the features to retrieve

**peek**: bool, optional

A boolean with a default of False. 
If it is set to true, the function only retrieve the first 50 rowsof each selected feature to save memory.

### Returns
pd.DataFrame
    A dataframe that contains the features of interest