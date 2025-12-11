#!python3

import sys
import os
from PyPDF2 import PdfReader, PdfMerger, PdfWriter

os.system("cls")

def rotatePDFPages(inPDFFile0, outputDirectory, rotationDegrees) :
    try :
        if not os.path.exists(outputDirectory) :
            os.makedirs(outputDirectory)
            output_path = os.path.join(outputDirectory, f"rotated_{os.path.basename(inPDFFile)}")
            with open(inPDFFile, "rb") as PdfToRotate :
                readerObject = PdfReader(PdfToRotate)
                writerObject = PdfWriter()
                
                for extractedPage in readerObject.pages :
                    extractedPage.rotate(rotationDegrees)
                    writerObject.add_page(extractedPage)
                    
                with open(output_path, "wb") as rotatePdfFile :
                    writerObject.write(rotatePdfFile)
                
            return f"Rotated PDF is saved to : {output_path}"
    except FileNotFoundError as fileNotFoundObject :
        print(f"Error: The given file {inPDFFile} doesnot exists", end = "\n")
        print(f"Message from Interpretor is : {fileNotFoundObject}", end="\n")
    except PermissionError as permissionErrorObject :
        print(f"Error: Permission denied to read the file {inPDFFile} OR write the output to {outputDirectory}", end = "\n")
        print(f"Message from Interpretor is : {permissionErrorObject}", end="\n")
    except Exception as exceptionObject :
        print(f"Error: Unexpected error encountered", end = "\n")
        print(f"Message from Interpretor is : {exceptionObject}", end="\n")
         

if __name__ == "__main__" :
    pdfFilePath = r"C:\Practice\my-python-journey\DataSets\PdfFiles\Sample.pdf"
    try :
        inPDFFile = r"C:\Practice\my-python-journey\DataSets\PdfFiles\Sample.pdf"
        outputDirectory = r"C:\Practice\my-python-journey\DataSets\OutData\RotatePdfFiles"
        rotationDegrees = int(input("\nPlease enter the Rotation degrees (90, 180, 270, -90, -180, -270) : "))
        if rotationDegrees not in[90, 180, 270, -90, -180, -270] :
            raise ValueError("Fatal Error! Rotation degrees must be one of the following : 90, 180, 270, -90, -180, -270")
            
        rotateResult = rotatePDFPages(inPDFFile, outputDirectory, rotationDegrees)
        print(rotateResult)
    except ValueError as valueErroObject :
        print(f"Hey! Encountered an error : {valueErroObject}", end="\n")
    except Exception as exceptionObject :
        print(f"Error: /Unexpected error encountered", end="\n")
        print(f"Message from interpretor is : {exceptionObject}", end="\n")
  
        

"""
Output:
-------

"""