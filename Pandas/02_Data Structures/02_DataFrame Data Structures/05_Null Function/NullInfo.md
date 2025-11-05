### Handling missing data in Pandas Dataframe:

1. Major part of the streaming data can contain missing values, due to operational non-availability of the system.
2. Missing data is treated by Pandas as `Not Available: NA` values
3. Missing data can become part of the Pandas data frame in a real stream, because
    1. The data is existing, but it was not collected by the data frame
    2. The data in reality is not existing
4. The missing data in Pandas is represented by two internally identified values
    1. None
        - **None** is in reality core Pythons `Singleton Object`, that is used by the developer for representing missing data
    2. NaN
        - **NaN** is and abbreviated form for `Not a Number`
        - NaN internally is a special kind of floating point value recognized universally in all the systems and technologies that support and follow IEEE floating point representations.
5. To convert `None` OR `NaN` python provides different functions
    - isnull()
    - botnull()
    - dropna()
    - fillna()
    - replace()
    - interpolate()

### How do we check missing values in Pandas dataframe?
1. When a missing value is part of the Pandas dataframe, we should use either `isnull()` OR `notnull()` functions to check the missing value status.
2. `isnull()` OR `notnull()` both will check whether the value is NaN OR not.
3. `isnull()` OR `notnull()` functions can also be used to find missing values in the Pandas Series.
4. When `isnull()` function is used upon a Pandas dataframe, the function returns the dataframe with boolean value of `True` for NaN number.
