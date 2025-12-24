### Time Module in Python :
1. According to Python Time is an object, hence the programmer cannot consider the Time in Python as a String OR a Timestamp.
2. To operate upon the Time we need to have the access to the Time Module class
3. To get proper accuracy upon the time, we have to set the required Timezone before operating upon the Time module.
4. For any software that is installed and configured upon the computer it asscociated to the hardware clock running on the machine, and in turn integrated to the Operating System Time management system calls.
5. The format of the Pre-programmed clock is : Date, Time and Timezone


### Points to check Before Operating with the Python Time Module :
1. The Time module in Python is actually wrapped upon the  `C` language runtime library, providing the functions for `time manipulation`.
2. The set of functions provided by Python can integrate with the system time through the `C Runtime Libraries`.
3. The Python time module follows the EPOCH convention, which technically defines the starting point of the time, which is supported by the dates and times from the EPOCH year as 2038.
4. The UNIX EPOCH time is `Midnight on 12:00 A.M. January 1st 1970`.
5. System to system with respect to the operating system and the corresponding software the EPOCH time can change.

```
import time
time.gmtime(0) # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
```

#### Note:
1. gmtime(0) method actually returns the `struct_time` object.

### What is actually meant by `tick` in Python ?
1. In practicality we have a term called as `Seconds since the EPOCH`, this represents the time in seconds that is elapsed since `EPOCH`.
2. `tick` in Python refers to the time interval which is a floating point number measured as `units of seconds`

### What is meant by DST (Daylight Saving Time) Format?
1. Certain function in Python Time module use DST format, which is a mechanism to move the clock `forward by 1 hour` during Summer and `backward by 1 hour` in Winter/Fall.

- `time.time()` - return number of fractional seconds in EPOCH time
- `time.process_time()` - This retunrs the sum of the system and the User CPU time of the current process, this function ignores the time elapsed during the sleep. 
- `time.perf_counter()` - This function uses a clock with the highest precision to measure the short duration and factors in the process sleep time.

### What are th ecomponents of the `time` tuple ?
0. 4-digit year
1. Month (1 to 12)
2. Month Day(1 to 31)
3. Hour (0 to 23)
4. Minutes (0 to 59)
5. Seconds (0 to 59)(0 to 61, where 60 and 61 are leap-seconds)
6. Day of the week (0 to 6, where 0 is Monday)
7. Day of the Year (1 to 366)
8. Day light savings (-1, 0, 1)