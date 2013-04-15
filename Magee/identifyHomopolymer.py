# Author: Nitesh Turaga
# Systems Programmer II, Lab - Adrian lee, Magee Womens Research Institute

# Description:
#   To do for identification of Homopolymer:
#   1. Navigate to the position in the variant file in the corresponding sequence.
#   2. Once at that position, check if the substitution at that position
#       gives rise to a homopolymer
#   3. If YES == HOMOPOLYMER at that position
#       then
#       dictionary = (key = sequence , value = (site of change, substitution))

import re
import commands
import math
import glob


def homopolymer(seq,pos):
    #sequence of gene, integer value of position of mutation
    substring = seq[pos-2]+seq[pos-1]+seq[pos]+seq[pos+1]+seq[pos+2]
    if (substring.count("a")>3 or substring.count("t")>3 or
        substring.count("g")>3 or substring.count("c")>3):
        return True
    else:
        return False

def identify(variantsFile):
    writeFileName = "homoplymer_%s" % (variantsFile)
    writeFile = open(writeFileName,"wt")
    text = "Chrom\tPosition\tPosition-Mut\tGene-Sym\tTarget-ID\tType\tPloidy\tRef\tVariant\tVar-Freq\tP-value\tCoverage\tRef-Cov\tVar-Cov\tRef-seq\tRef-seq-start\tRef-seq-End\tVariant-seq\tMutation-Pos\tHomopolymer\n"
    count = 0
    for line in open(variantsFile):
        #Open variants file and get gene and mutation-position. 
        count +=1
        gene = line.split(" ")[0].split("\t")[3]
        mutationPosition = line.split(" ")[0].split("\t")[1]
        
        #Make specific file name
        filename =str(count)+"_" + gene + "_das.txt_seq.txt"

        #OPEN Specific file
        x= open(filename,"r")
        seqFile = x.read()
        x.close()
    
        seq = seqFile.split("\t")[0]
        # pos = mutationPostion - start position of gene
        pos = int(mutationPosition) -int(seqFile.split("\t")[1])
        
        change = line.split("\t")[8]
        changeSeq = seq[:25] + change + seq[26:]
        print changeSeq
        if (homopolymer(seq,pos)==True):
            #format = Sequence, index of mutation, position number of mutation
            
            lineToWrite = line.replace("\n","\t") + seqFile.replace("\n","") + "\t" + changeSeq +"\t"+str(pos) + "\t"+"YES"+"\n"
            if not lineToWrite in text:
                text +=lineToWrite
                
        else:
            
            lineToWrite = line.replace("\n","\t") + seqFile.replace("\n","") + "\t" + changeSeq +"\t"+str(pos) + "\t"+"NO"+"\n"
            if not lineToWrite in text:
                text +=lineToWrite
    writeFile.write(text)
    return

            
identify("HCC1954_variants.txt")

                                
