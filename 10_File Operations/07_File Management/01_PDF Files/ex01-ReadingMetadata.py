#!python3

import os
from PyPDF2 import PdfReader

os.system("cls")

def extract_PDFInformation(inPDFFilePath) :
    with open(inPDFFilePath, "rb") as inPDFFile :
        pdfInformation = PdfReader(inPDFFile)
        
        pdfDocInfo = pdfInformation.metadata
        pdfDocPages = len(pdfInformation.pages)
        
        metaDataInfo = f"""
            The Metadata Imformation About the PDF file : {inPDFFilePath} :
            Author : {pdfDocInfo.author if pdfDocInfo.author else "No Author"}
            Creator : {pdfDocInfo.creator if pdfDocInfo.creator else "No Creator"}
            Producer : {pdfDocInfo.producer if pdfDocInfo.producer else "No Producer"}
            Subject : {pdfDocInfo.subject if pdfDocInfo.subject else "No Subject"}
            Title : {pdfDocInfo.title if pdfDocInfo.title else "No Title"}
            Number of Pages : {pdfDocPages}
        """
        print(metaDataInfo)
        
        return pdfDocInfo
    
if __name__ == "__main__" :
    pdfFilePath = r"C:\Practice\my-python-journey\DataSets\PdfFiles\Sample.pdf"
    extract_PDFInformation(pdfFilePath)
    

"""
Output:
-------
The Metadata Imformation About the PDF file : C:\Practice\my-python-journey\DataSets\PdfFiles\Sample.pdf :
Author : No Author
Creator : Writer
Producer : LibreOffice 4.2
Subject : No Subject
Title : No Title
Number of Pages : 4
"""