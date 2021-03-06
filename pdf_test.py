import os
import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    print(path)
    fp = file(path, 'rb')
    print('Found your file :)')
    print('Processing "%s"' % path)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text
print('Author-tanishqCIC')
print('Build initialised')
print('NOTE: Make sure file is in the same folder')
fname = raw_input('Enter file[PDF] name : ')
#fname='cikm2011a.pdf'
text = convert_pdf_to_txt(fname)
print('Writing ino .txt file')
text_file = open('%s.txt' % fname[:-4], 'w')
text_file.write(text)
text_file.close
print('Check out the file named "%s.txt"' % fname[:-4])


