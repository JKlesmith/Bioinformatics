#!/usr/bin/python

#Copyright (c) 2016, Justin R. Klesmith
#All rights reserved.

from __future__ import division
from math import log, sqrt, pow
import argparse, os, random

#Set the author information
__author__ = "Justin R. Klesmith"
__copyright__ = "Copyright 2016, Justin R. Klesmith"
__credits__ = ["Justin R. Klesmith", "Timothy A. Whitehead"]
__license__ = "BSD-3"
__version__ = "X.X, Build: 2016XXXX"
__maintainer__ = "Justin R. Klesmith"
__email__ = ["klesmit3@msu.edu", "justinklesmith@gmail.com", "justinklesmith@evodyn.com"]

#Get commandline arguments
parser = argparse.ArgumentParser(description='Process the MSA to get into a format for PSI-Blast')
parser.add_argument('-m', dest='msa', action='store', required=True, help='MSA file path')
parser.add_argument('-l', dest='length', action='store', required=True, help='Length of protein')
#parser.add_argument('-d', dest='dssp', action='store', required=True, help='Path to processed DSSP output')
args = parser.parse_args()

#Populate array
Mutations = {}
for j in xrange(1,int(args.length)):
    #Mutations[j] = False
    Mutations[j] = None

#Import DSSP Information from CSV
#if os.path.isfile(args.dssp):
#    with open(args.dssp, 'r') as infile: #Open the file with the wild-type protein sequence
#        for line in infile:
#            split = line.split(",")
#            if split[0] != "ID": #Skip the CSV header
#                location = int(split[0])
#                ss = str(split[1]).rstrip("\n\r")
#                
#                if len(ss) == 0:
#                    Mutations[location] = "L"
#                else:
#                    Mutations[location] = ss
                #If loop then set true
                #if len(ss) == 0 or ss == "S" or ss == "T":
                    #Mutations[location] = True
#else:
#    print "Cannot open the processed DSSP"
#    quit()    
    
#Import msa alignment
Alignment = ""
outfile = open('msatemp.csv', 'w')
if os.path.isfile(args.msa):
    with open(args.msa, 'r') as infile: #Open the file with the wild-type protein sequence
        Output = ""
        
        for line in infile:
        
            #Check to see if we have a header
            if line[0] == ">":
                #print Output #Print the current alignment
                Alignment = Alignment + Output + "\n"
                
                
                Output = "" #Empty the current alignment
                Output = Output + line.rstrip('\n') + "," #Assemble the line
            else:
                Output = Output + line.rstrip('\n') #Assemble the line
else:
    print "Cannot open the processed NCBI CSV"
    quit()
outfile.write(Alignment)
outfile.close()

#Import MSA into a lookup table
MSATable = {}
outfile = open('msatemp2.csv', 'w')
with open('msatemp.csv', 'r') as infile: #Open the file with the wild-type protein sequence
    for line in infile:
        split = line.split(",")
        if len(line) > 10:
            MSATable.update({split[0] : split[1].rstrip("\n")})
            outfile.write(split[1])

outfile.close()

#Make a DSSP lookup string
Wildtype = MSATable[">ENTER YOUR WILD-TYPE SEQUENCE HEADER NAME HERE found in the MSA or CDHIT Cluster"]
MSAWTLen = len(Wildtype)
#CorrectedDSSP = ""
#DSSPCount = 1

#print Wildtype
#DSSP = ""
#for j in xrange(1,int(args.length)):
    #Mutations[j] = False
    #DSSP =  DSSP + Mutations[j].rstrip("\n\r")
#print DSSP    
    
#for j in xrange(0,MSAWTLen):
#    if Wildtype[j] == "-":
#        CorrectedDSSP = CorrectedDSSP + "-"
#    else:
#        CorrectedDSSP = CorrectedDSSP + Mutations[DSSPCount]
#        DSSPCount = DSSPCount + 1

#Add the lookup string to the 2nd temp table
#with open('msatemp2.csv', 'r+') as f:
#    content = f.read()
#    f.seek(0, 0)
#    f.write(CorrectedDSSP + '\n' + Wildtype + '\n\n' + content)
    
#Time to mark the insertions
XedOut = ""
outfile2 = open('msatemp3.csv', 'w')
Wildtype = Wildtype + "\n"
MSAWTLen = len(Wildtype)
with open('msatemp2.csv', 'r') as f:
    for line in f:
        for i in xrange(0,MSAWTLen):
            if Wildtype[i] == "-":
                XedOut = XedOut + "X"
            else:
                XedOut = XedOut + line[i]
outfile2.write(XedOut)
outfile2.close()

#Now let's delete the insertions
output = ""
with open('msatemp3.csv', 'r') as f1:
    for line in f1:
        Len = len(line)
        for i in xrange(0, Len):
            if line[i] != "X":
                output = output + line[i]

f1o = open('msatemp4.csv', 'w')
f1o.write(output)
f1o.close()

#to make the fifth file sequences that lacked the length and lgk3
output = ""
with open('msatemp5.csv', 'r') as f2:
    for line in f2:
        output = output + ">" + str(random.random()) + "\n" + line + "\n"

f1o = open('msatemp6.csv', 'w')
f1o.write(output)
f1o.close()