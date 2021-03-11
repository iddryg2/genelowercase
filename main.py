# A script to convert every gene name to capitalized first letter, every other letter lowercase.
# This is to convert a gene set for GSEA. https://www.gsea-msigdb.org/gsea/index.jsp
# It is a tab-delimited text file.
# March 2021 - Ian Dryg

import csv
import string

def capper(mystr):
    for idx, i in enumerate(mystr):
        if not i.isdigit():  # or if i.isalpha()
            return ''.join(mystr[:idx] + mystr[idx:].capitalize())
    return mystr


filepath = '/Users/drygi01/Documents/R/Maria-RNAseq/GSEA 2021/try2_preranked/'
with open(filepath + 'ExhaustionUpDown3.txt', 'r', newline='') as inputfile, open(filepath + 'ExhaustionUpDown5.txt', 'w', newline='') as outputfile:
    reader = csv.reader(inputfile, delimiter='\t')
    writer = csv.writer(outputfile, delimiter='\t')
    for geneset in reader:
        for item in geneset:
            print(item)
            print(capper(item))
            # convert to capitalized, lowercase gene name and write to outputfile.
            outputfile.write(capper(item) + '\t')
        outputfile.write('\n')


