#!/usr/bin/env python

'''
    truncate.py: In order to use this script you must first open your PGN file in notepad and 'Save As' txt file (For Efficiency).
                 Truncate a PGN file of many chess games down to the first 20 moves (Or however many you want). 
                 It then outputs a new txt file without any moves after the 20th move. You can open this file in notepad and 'Save As' PGN file.
                                                                                                                                                '''
__author__ = "PassZ"
__version__ = "1.0.0"

#Imports
import sys
import re
import os

# Make sure the user provides the correct number of command-line arguments
if len(sys.argv) < 3:
    print("Usage: python truncate.py input.txt output.txt")
    sys.exit(1)

# Get the input and output file names from the command line
input_file = sys.argv[1]
output_file = sys.argv[2]

# Open the output PGN file that we are writing to
with open(output_file, "w", encoding="utf-8-sig") as output:

    # Open the input PGN file that we are reading from
    with open(input_file, encoding="utf-8-sig", errors='ignore') as input:

        # Read the contents of the input file
        contents = input.read()

        # Truncate the contents of the input file with a regular expression
        s = re.sub('21\.(.*?)(\n.*?)*(1\/2\-1\/2|1\-0|0\-1)', '', contents)

    # Write the truncated contents to the output file
    output.write(s)