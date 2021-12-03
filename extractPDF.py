#!/usr/bin/python

"""
Extracts a page range into a new PDF.
"""

import sys
import os
import argparse
import PyPDF2

parser = argparse.ArgumentParser(description='Extract pages from a PDF into a new pdf')
parser.add_argument('--input', type=str, help='path to input file')
parser.add_argument('--start', type=int, help='start index (inclusive)')
parser.add_argument('--end', type=int, help='end index (inclusive)')                   
parser.add_argument('--output', type=str, help='path to output file')
args = parser.parse_args()

original_reader = PyPDF2.PdfFileReader(args.input)

new_file = PyPDF2.PdfFileWriter()
for page_index_from_zero in range((args.start-1), (args.end-1)+1):
  #pages are zero-indexed; need the following page index for python indexing
  print('Adding page '+str(page_index_from_zero+1)+'...')
  page = original_reader.getPage(page_index_from_zero)
  new_file.addPage(page)

print('Saving to new file...')
out_file = open(args.output, 'wb')
new_file.write(out_file)
out_file.close()