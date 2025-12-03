1. To read the excel files in Pandas, need to install `openpyxl` package.
    - `pip install openpyxl`
    - `pd.read_excel(filepath)`

2. reading xml file formats, use
    - `import xml.etree.ElementTree as ET`
    - `ET.parse(filePath)`

3. To show the data in tabular format, need `tabulate` package.
    - `pip install tabulate`
    - `from tabulate import tabulate`
    - table formats are `grid/mysql/plain`

4. We can't use reduce function directly
    - First import `functools`
    - use functools.reducce() function