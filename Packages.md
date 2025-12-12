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
5. Working on audio/video files, need to install `playsound` package.
```
    1. If higher version of playsound is not supported then 
    1. Uninstall playsound if already installed
        pip uninstall playsound
    2. Install playsound
        pip install playsound==1.2.2
```
6. Handling pdf files in Python use - 
    1. PyPDF2
    2. ReportLab
    3. PDFMiner.six
    4. PikePDF