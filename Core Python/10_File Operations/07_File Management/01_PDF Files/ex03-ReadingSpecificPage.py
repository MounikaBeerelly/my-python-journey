#!python3

import os
from PyPDF2 import PdfReader

os.system("cls")

def readAllPages(inFilePath) :
    pdfPagesText = []
    try :
        with open(inFilePath, "rb") as myPdfFile :
            readerObject = PdfReader(myPdfFile)
            
            if readerObject.is_encrypted :
                readerObject.decrypt("")
                
            numberOfPages = len(readerObject.pages)
            
            for outPageNumber in range(numberOfPages) :
                pageObject = readerObject.pages[outPageNumber]
                pageData = pageObject.extract_text()
                pdfPagesText.append(pageData)
    except Exception as exceptionObject :
        print(f"\nHey! Encountered an Error : {exceptionObject}\n")
        
    return pdfPagesText
    
def readCustomPageInfo(inFilePath, inPageNumber) :
    pageText = None
    
    try :
        with open(inFilePath, "rb") as myPdfFile :
            readerObject = PdfReader(myPdfFile)
            
            if readerObject.is_encrypted :
                readerObject.decrypt("")
                
            numberOfPages = len(readerObject.pages)
            
            if(inPageNumber < 1 or inPageNumber > numberOfPages) :
                raise ValueError("\nFatal Error! PAge number is out of range..")
            
            outPageObject = readerObject.pages[inPageNumber - 1]
            pageText = outPageObject.extract_text()
    except Exception as exceptionObject :
        print(f"\nHey! Encountered an Error.. : {exceptionObject}\n")
    
    return pageText
        
if __name__ == "__main__" :
    pdfFilePath = r"C:\Practice\my-python-journey\DataSets\PdfFiles\Sample.pdf"
    
    print("\nReading PDF file... \n-------------- \n1.Read all pages\n2.Read specific page\n", end="\n")
    inReadChoice= int(input("\nPlease enter your reading choice from the menu (1 : Read all pages, 2 : Read specific page) : "))
    
    if inReadChoice == 1 :
        allPagesInfo = readAllPages(pdfFilePath)
        for pageIndex, outPageText in enumerate(allPagesInfo, start = 1) :
            print(f"\nNow printing page number {pageIndex} : \n\n{outPageText}")
    elif inReadChoice == 2 :
        inPageNumber = int(input("\nPlease enter the page number to read : "))
        readCustomPageInfo = readCustomPageInfo(pdfFilePath, inPageNumber)
        if readCustomPageInfo : 
            print(f"\nNow printing the data from pagenumber {inPageNumber} : \n\n{readCustomPageInfo}")
        else : 
            print(f"\nSorry! the given page number {inPageNumber} is a blank page..")
"""
Output:
-------

Reading PDF file...
--------------
1.Read all pages
2.Read specific page


Please enter your reading choice from the menu (1 : Read all pages, 2 : Read specific page) : 2

Please enter the page number to read : 2

Now printing the data from pagenumber 2 :

In non mauris justo. Duis vehicula mi vel mi pretium, a viverra erat efficitur. Cras aliquam
est ac eros varius, id iaculis dui auctor. Duis pretium neque ligula, et pulvinar mi placerat
et. Nulla nec nunc sit amet nunc posuere vestibulum. Ut id neque eget tortor mattis
tristique. Donec ante est, blandit sit amet tristique vel, lacinia pulvinar arcu. Pellentesque
scelerisque fermentum erat, id posuere justo pulvinar ut. Cras id eros sed enim aliquam
lobortis. Sed lobortis nisl ut eros efficitur tincidunt. Cras justo mi, porttitor quis mattis vel,
ultricies ut purus. Ut facilisis et lacus eu cursus.
In eleifend velit vitae libero sollicitudin euismod. Fusce vitae vestibulum velit. Pellentesque
vulputate lectus quis pellentesque commodo. Aliquam erat volutpat. Vestibulum in egestas
velit. Pellentesque fermentum nisl vitae fringilla venenatis. Etiam id mauris vitae orci
maximus ultricies.
Cras fringilla ipsum magna, in fringilla dui commodo
a.
Lorem ipsum Lorem ipsum Lorem ipsum
1 In eleifend velit vitae libero sollicitudin euismod. Lorem
2 Cras fringilla ipsum magna, in fringilla dui commodo
a.Ipsum
3 Aliquam erat volutpat. Lorem
4 Fusce vitae vestibulum velit. Lorem
5 Etiam vehicula luctus fermentum. Ipsum
Etiam vehicula luctus fermentum. In vel metus congue, pulvinar lectus vel, fermentum dui.
Maecenas ante orci, egestas ut aliquet sit amet, sagittis a magna. Aliquam ante quam,
pellentesque ut dignissim quis, laoreet eget est. Aliquam erat volutpat. Class aptent taciti
sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Ut ullamcorper
justo sapien, in cursus libero viverra eget. Vivamus auctor imperdiet urna, at pulvinar leo
posuere laoreet. Suspendisse neque nisl, fringilla at iaculis scelerisque, ornare vel dolor. Ut
et  pulvinar  nunc.  Pellentesque  fringilla  mollis  efficitur.  Nullam  venenatis  commodo
imperdiet. Morbi velit neque, semper quis lorem quis, efficitur dignissim ipsum. Ut ac lorem
sed turpis imperdiet eleifend sit amet id sapien.

"""