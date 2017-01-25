import argparse, os, random

#Get commandline arguments
parser = argparse.ArgumentParser(description='Remove sequences with indels')
parser.add_argument('-m', dest='msa', action='store', required=True, help='MSA file path')
args = parser.parse_args()

#Assign sequence regions to LGK using DSSP as a guide (the 160 longest constructs was used) (this is after the X marked insertions are deleted)
Regions = [[0,10], [11,35], [36,47], [48,98], [99,107], 
[108,117], [118,128], [129,195], [196,207], 
[208,226], [227,237], [238,260], [261,273], 
[274,313], [314,320], [321,341], [342,345], 
[346,374], [375,393], [394,410], [411,423],
[424,433], [434,438]]
NumRegions = 23

#Lets open the MSA (one sequence per line)
if os.path.isfile(args.msa):
    with open(args.msa, 'r') as infile: #Open the file with the wild-type protein sequence
        
        for region in Regions:
            Start = region[0]
            End = region[1]
            
            infile.seek(0)
            outfile = open('Subalignment_start'+str(Start)+'.csv', 'w')
            for line in infile:
                Subline = ""
                for i in xrange(Start,End+1):
                    Subline = Subline + line[i]
                
                #Remove sequences with insertions
                if Subline.find('-') == -1:
                    outfile.write(">" + str(random.random()) + "\n")
                    outfile.write(Subline + "\n")
            
            outfile.close()