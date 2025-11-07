### Note:
---------

Handle auto conversion of large datasets : `pd.set_option('display.float_format','{:.0f}'.format)`

## Working on Multiple Datasets in Pandas:

1. Every Pandas Dataframe is a two-dimensional data structure representing the data in Rows and Columns.
2. Pandas dataframe is basically
    1. Two Dimensional Size-mutable
    2. Can carry heterogeneous tabular data
    3. Can be represented with labelled axes, where one axis is Rows and the second axis is columns
3. Upon the Pandas dataframe we can execute different methods like 
    1. Merging of the dataframes
    2. Concatinating of the dataframes
    3. Joining of the dataframes


### Executing the concatination Operation upon the Pandas dataframe :

1. Pandas dataframes can be concatenated using the `concat()` function
2. By practically we can concatenate the Dataframes in multiple different ways using
    1. dataFrameObject.concat() method
    2. Setting the logic on the dataframe axes
    3. Using dataFrameObject.append() methos
    4. By ignoring the indexes of the dataframes
    5. By using the group keys
    6. With the help of mixed `ndims`