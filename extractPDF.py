#!/usr/bin/python

"""
xtracts a page range into a new PDF.
"""

import sys
import os
import argparse
from CoreGraphics import *


parser = argparse.ArgumentParser(description='Extract pages from a PDF into a new pdf')
parser.add_argument('--input', type=str, help='path to input file')
parser.add_argument('--start', type=int, help='start index (inclusive)')
parser.add_argument('--end', type=int, help='end index (inclusive)')                   
parser.add_argument('--output', type=str, help='path to output file')
args = parser.parse_args()

inputDoc = CGPDFDocumentCreateWithProvider(CGDataProviderCreateWithFilename(args.input))

if inputDoc:
  maxPages = inputDoc.getNumberOfPages()  
else:
  sys.exit(2)

print('Extracting pages '+str(args.start)+' to '+str(args.end)+' of '+args.input +' to new file '+args.output)

pageRect = CGRectMake (0, 0, 612, 792)
writeContext = CGPDFContextCreateWithFilename(args.output, pageRect)
for pageNum in range(args.start, args.end + 1):
  mediaBox = inputDoc.getMediaBox(pageNum)
  writeContext.beginPage(mediaBox)
  writeContext.drawPDFDocument(mediaBox, inputDoc, pageNum)
  writeContext.endPage()
