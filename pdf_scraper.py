import os
import slate3k as slate
import PyPDF2

# recruiterlist.pdf is in the desktop

# Scrapes the text from the PDF file (not accurate)
def pdf_scraper():
    os.chdir('c:\\Users\\Mira\\Desktop')
    with open('recruiterlist.pdf','rb') as f:
        extracted_text = slate.PDF(f)
    return extracted_text

# Calculates the number of pages
def pdf_pagecount():
    os.chdir('c:\\Users\\Mira\\Desktop')
    pdfFile = open('recruiterlist.pdf','rb')
    reader = PyPDF2.PdfFileReader(pdfFile)
    return reader.numPages

# Puts the text by page number into an array
def arr_count():
    arr = []
    for i in range(pdf_pagecount()):
        arr.append(pdf_scraper()[i])
    return arr
