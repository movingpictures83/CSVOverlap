# CSVOverlap
# Language: Python
# Input: TXT 
# Output: CSV 
# Tested with: PluMA 1.1, Python 3.6
# Dependency: numpy==1.16.0

CSVMerge is a PluMA plugin that expects as input a .txt file containing
two lines of keyword-value pairs, tab-delimited:

csvfile1: First vector (assumed to be second column of CSV)
csvfile2: Second vector (assumed to be second column of CSV)

The output CSV file will contain the overlap (second column).

