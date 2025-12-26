#!python3

import os
from PyPDF2 import PdfReader, PdfWriter

os.system("cls")

def addWaterMark(inPDFFile, waterMarkPDF, outputPDF):
    try:
        # Ensure output directory exists
        output_dir = os.path.dirname(outputPDF)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Read main PDF
        readerObject = PdfReader(inPDFFile)

        # Read watermark PDF
        waterMarkReader = PdfReader(waterMarkPDF)
        waterMarkPage = waterMarkReader.pages[0]

        writerObject = PdfWriter()

        # Merge watermark on each page
        for page in readerObject.pages:
            # Important: create a COPY for merging
            page.merge_page(waterMarkPage)
            writerObject.add_page(page)

        # Write output
        with open(outputPDF, "wb") as outPdf:
            writerObject.write(outPdf)

        print(f"\nWatermark added successfully!\nOutput: {outputPDF}")

    except FileNotFoundError as e:
        print(f"Error: File not found → {e}")

    except Exception as e:
        print(f"Unexpected error → {e}") 

if __name__ == "__main__":
    try:
        inPDFFile = r"C:\Practice\my-python-journey\DataSets\PdfFiles\index.pdf"
        waterMarkPdffile = r"C:\Practice\my-python-journey\DataSets\PdfFiles\Watermark.pdf"
        outputFile = r"C:\Practice\my-python-journey\DataSets\OutData\WaterMarkFiles\wmPdfFile.pdf"

        addWaterMark(inPDFFile, waterMarkPdffile, outputFile)

    except Exception as e:
        print(f"ERROR → {e}")
