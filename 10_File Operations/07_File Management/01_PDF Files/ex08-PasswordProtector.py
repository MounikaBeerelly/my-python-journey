#!python3

import os
from PyPDF2 import PdfReader, PdfWriter

os.system("cls")

def applyPassword(inPDFFile, outputDirectory, inPassword) :
    try :
        pdfReaderObject = PdfReader(inPDFFile)
        pdfWriterObject = PdfWriter()
        
        numberOfPages = len(pdfReaderObject.pages)
        
        for extractedPage in range(numberOfPages) :
            pdfWriterObject.add_page(pdfReaderObject.pages[extractedPage])
            
            pdfWriterObject.encrypt(user_password = inPassword, owner_pwd = None, use_128bit = True)
            
        with open(outputDirectory, mode = "wb") as outPasswordPDF :
            pdfWriterObject.write(outPasswordPDF)
            
        print(f"Success! Your PDf password protected and saved in : {outputDirectory}", end="\n")
    except FileNotFoundError as fileNotFoundObject :
        print(f"Error: The given file {inPDFFile} doesnot exists", end = "\n")
        print(f"Message from Interpretor is : {fileNotFoundObject}", end="\n")
    except PermissionError as permissionErrorObject :
        print(f"Error: Permission denied to read the file {inPDFFile} OR write the output to {outputDirectory}", end = "\n")
        print(f"Message from Interpretor is : {permissionErrorObject}", end="\n")
    except Exception as exceptionObject :
        print(f"Error: Unexpected error encountered", end = "\n")
        print(f"Message from Interpretor is : {exceptionObject}", end="\n")
         

if __name__ == "__main__":
    try:
        inPDFFile = r"C:\Practice\my-python-journey\DataSets\PdfFiles\sample.pdf"
        outputDirectory = r"C:\Practice\my-python-journey\DataSets\OutData\ProtectedPDF\ProtectedPDFFile.pdf"
        inPassword = input("Enter the password : ")
        applyPassword(inPDFFile, outputDirectory, inPassword)
    except Exception as e:
        print(f"ERROR → {e}")

"""
Output:
-------
Enter the password : skyess
Success! Your PDf password protected and saved in : C:\Practice\my-python-journey\DataSets\OutData\ProtectedPDF\ProtectedPDFFile.pdf
"""