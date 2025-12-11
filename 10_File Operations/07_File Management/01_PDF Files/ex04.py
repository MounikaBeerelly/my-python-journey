#!python3

import sys
import os
from PyPDF2 import PdfReader, PdfMerger

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
        
def mergePDFFile(pdfFiles2Merge, outMergeFile) :
    pdfMergeObject = PdfMerger()
     
    for outPDFFile in pdfFiles2Merge :
        pdfMergeObject.append(outPDFFile)
         
    pdfMergeObject.write(outMergeFile)
    pdfMergeObject.close()
    
    return
     
if __name__ == "__main__" :
    pdfFilePath = r"C:\Practice\my-python-journey\DataSets\PdfFiles\Sample.pdf"
    
    print("\nReading PDF file... \n-------------- \n1.Read all pages\n2.Read specific page\n3.Merge PDFs", end="\n")
    inReadChoice= int(input("\nPlease enter your reading choice from the menu (1 : Read all pages, 2 : Read specific page, 3 : Merge PDFs) : "))
    
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
    elif inReadChoice == 3 :
        inPDFFile01 = r"C:\Practice\my-python-journey\DataSets\PdfFiles\index.pdf"
        inPDFFile02 = r"C:\Practice\my-python-journey\DataSets\PdfFiles\drylab.pdf"
        
        pdfFiles2Merge = [inPDFFile01, inPDFFile02]
        outMergedFile = r"C:\Practice\my-python-journey\DataSets\OutData\MergedPDFFiles\001_MergedFile.pdf"
        mergePDFFile(pdfFiles2Merge, outMergedFile)
    else : 
        print("Sorry! Invalid input detected... Esisting the application..", end="\n")
        sys.exit()
        
