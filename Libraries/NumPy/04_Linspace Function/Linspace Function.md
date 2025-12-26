## Linspace function:
 
1. The `np.linspace()` function in NumPy generates evenly spaced values between a specified start and stop value over a defined number of points.
2. `np.linspace()` focuses on the number of points and ensures equal spacing

### Basic Syntax:

    `numpy.linspace(start,stop,num=50, endpoint=True, restep=False, dtype=none, axis=0)`

- **start**: The starting value of the sequence
- **stop**: The ending value of the sequence
- **num**: (Optional) The number of points to generate. Default is 50
- **endpoint**: (Optional) If true (default), includes the stop value; otherwise, excludes it
- **retstep**: (Optional) If True, returns the spacing between points along with the array
- **dtype**: (Optional) specifies the desired data type of the output array
- **axis**: (Optional) Axis in the result along which the values are stored

Where to use?
-------------
1. Ideal for generating fixed-size arrays with precise spacing
2. Ensures the array covers the specified range with or without including the stop value
