#!/bin/python

#Copyright (c) 2015, Justin R. Klesmith
#All rights reserved.
#CodonSwap: Swap codons for synonymous mutations

import argparse
import os

#Set the author information
__author__ = "Justin R. Klesmith"
__copyright__ = "Copyright 2015, Justin R. Klesmith"
__credits__ = ["Justin R. Klesmith", "Timothy A. Whitehead"]
__license__ = "BSD-3"
__version__ = "0.1, Build: 20150919"
__maintainer__ = "Justin R. Klesmith"
__email__ = ["klesmit3@msu.edu", "justinklesmith@gmail.com", "justinklesmith@evodyn.com"]

#Get commandline arguments
parser = argparse.ArgumentParser(description='CodonSwap '+__version__+' for swapping codons to synomymous mutations')
parser.add_argument('-w', dest='wildtype', action='store', nargs='?', const=1, default='./WTSeq', help='File with the wild-type DNA sequence. Default = ./WTSeq')
args = parser.parse_args()

if os.path.isfile(args.wildtype):
    with open(args.wildtype, 'r') as infile: #Open the file with the wild-type DNA sequence
        WTSeq = infile.readline() #Read the first line of the WT sequence file
else:
    print "Missing the wild-type DNA sequence file. Flag: -w or a file named WTSeq in the ./ directory. ...exit"
    quit()

AA_Table = '*ACDEFGHIKLMNPQRSTVWY'
Codon_Table = {'TTT':'F', 'TCT':'S', 'TAT':'Y', 'TGT':'C',
'TTC':'F', 'TCC':'S', 'TAC':'Y', 'TGC':'C',
'TTA':'L', 'TCA':'S', 'TAA':'*', 'TGA':'*',
'TTG':'L', 'TCG':'S', 'TAG':'*', 'TGG':'W',
'CTT':'L', 'CCT':'P', 'CAT':'H', 'CGT':'R',
'CTC':'L', 'CCC':'P', 'CAC':'H', 'CGC':'R',
'CTA':'L', 'CCA':'P', 'CAA':'Q', 'CGA':'R',
'CTG':'L', 'CCG':'P', 'CAG':'Q', 'CGG':'R',
'ATT':'I', 'ACT':'T', 'AAT':'N', 'AGT':'S',
'ATC':'I', 'ACC':'T', 'AAC':'N', 'AGC':'S',
'ATA':'I', 'ACA':'T', 'AAA':'K', 'AGA':'R',
'ATG':'M', 'ACG':'T', 'AAG':'K', 'AGG':'R',
'GTT':'V', 'GCT':'A', 'GAT':'D', 'GGT':'G',
'GTC':'V', 'GCC':'A', 'GAC':'D', 'GGC':'G',
'GTA':'V', 'GCA':'A', 'GAA':'E', 'GGA':'G',
'GTG':'V', 'GCG':'A', 'GAG':'E', 'GGG':'G'}
EColi_Table = {'TTT':'TTC', 'TCT':'AGC', 'TAT':'TAC', 'TGT':'TGC',
'TTC':'TTT', 'TCC':'AGT', 'TAC':'TAT', 'TGC':'TGT',
'TTA':'CTG', 'TCA':'TCG', 'TAA':'TAA', 'TGA':'TAA',
'TTG':'CTT', 'TCG':'TCA', 'TAG':'TGA', 'TGG':'TGG',
'CTT':'TTA', 'CCT':'CCC', 'CAT':'CAC', 'CGT':'CGC',
'CTC':'TTG', 'CCC':'CCT', 'CAC':'CAT', 'CGC':'CGT',
'CTA':'TTG', 'CCA':'CCG', 'CAA':'CAG', 'CGA':'AGA',
'CTG':'TTA', 'CCG':'CCA', 'CAG':'CAA', 'CGG':'CGA',
'ATT':'ATC', 'ACT':'ACA', 'AAT':'AAC', 'AGT':'TCC',
'ATC':'ATT', 'ACC':'ACG', 'AAC':'AAT', 'AGC':'TCT',
'ATA':'ATT', 'ACA':'ACT', 'AAA':'AAG', 'AGA':'CGA',
'ATG':'ATG', 'ACG':'ACC', 'AAG':'AAA', 'AGG':'AGG',
'GTT':'GTG', 'GCT':'GCA', 'GAT':'GAC', 'GGT':'GGC',
'GTC':'GTA', 'GCC':'GCG', 'GAC':'GAT', 'GGC':'GGT',
'GTA':'GTC', 'GCA':'GCT', 'GAA':'GAG', 'GGA':'GGG',
'GTG':'GTT', 'GCG':'GCC', 'GAG':'GAA', 'GGG':'GGA',}

def main():
    #Write out preamble
    print "CodonSwap - Swap codons to synonymous codons (optimized for E.coli codon usage)"
    print "Author: "+__author__
    print "Contact: "+__email__[0]+", "+__email__[1]+", "+__email__[2]
    print __copyright__
    print "Version: "+__version__
    print "License: "+__license__
    print "Credits: "+__credits__[0]+", "+__credits__[1]
    print ""
    print "Please cite:"
    print "Github [user: JKlesmith] (www.github.com)"
    print ""
    
    WTASeq = ""
    NewDNASeq = ""
    NewAASeq = ""

    for i in xrange(0,(len(WTSeq)/3)):
        WTASeq = WTASeq + str(Codon_Table[WTSeq[i*3:i*3+3]])
        NewDNASeq = NewDNASeq + str(EColi_Table[WTSeq[i*3:i*3+3]])
        NewAASeq = NewAASeq + str(Codon_Table[EColi_Table[WTSeq[i*3:i*3+3]]])
    
    print "Wild-type DNA sequence"
    print WTSeq.rstrip('\r\n')
    print "Codon swapped DNA sequence"
    print NewDNASeq
    print "Wild-type amino acid sequence"
    print WTASeq
    print "Codon swapped amino acid sequence"
    print NewAASeq
    
if __name__ == '__main__':
    main()