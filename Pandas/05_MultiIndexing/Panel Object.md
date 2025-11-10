## Panel in Python Pandas

1. Panel is a 3 dimensional container for managing the data.
2. Panel provides 3 axes for representing the data.
    1. **Items** -
        - Which is basically axis 0
        - Each item in the Panel represents to the dataframe that actually contains the data
    2. **Major_Axis** -
        - Which is basically axis 1
        - Axis 1 represents the index of rows of each of the data represented in the dataframe.
    3. **Minor_Axis** -
        - Which is basically axis 2
        - Axis 2 represents the index of columns of each of the data represented in the dataframe.

#### Panel is deprecated and no more supported in Pandas.

## Pandas MultiIndex.to_frame() :
1. MultiIndex.to_frame() function in Pandas will help in creating a dataframe with the levels of MultiIndex as columns.
