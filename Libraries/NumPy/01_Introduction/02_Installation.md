## Installing NumPy on Windows

- The most common methods involve using pip (python's package manager) OR Conda (If you're using Anaconda)

### Installing NumPy using pip:

**Prerequisites**:
- Make sure Python is installed on your system
- verify python: `python --version`
- verify pip: `pip --version`

**Note**: It is recommended to upgrade pip to the latest version
- `python -m pip install --upgrade pip`

**Install NumPy**
- `pip install numpy`

**Verify NumPy installtion**
- `STEP 01` - Open command prompt of the operating system
- `STEP 02` - Open Python shell by typing "py" at the command prompt
- `STEP 03` - Verify NumPy
    - import numpy as np
    - print(np.__version__)