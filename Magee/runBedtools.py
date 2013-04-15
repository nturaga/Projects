# Author: Nitesh Turaga
# Systems Programmer II, Lab - Adrian lee, Magee Womens Research Institute

# Description:

import re
import commands
import os
import glob
import subprocess

def makeFile(variantsFiles):
    count = 0
    
    ## SEPERATING BED FILES
    for line in open(variantsFiles):
        print line
        count +=1
        fileName = "%d-%s.bed" % (count,line.split("\t")[3])
        
        x = open(fileName,"wt")
        x.write(line)
        x.close()
 

    return
    # INTERSECT WITH BED FILE"S" with BAM FILE

def intersect(bamFile):
    path = "."
    for infile in glob.glob(os.path.join(path,'*.bed')):
        commands.getstatusoutput("bedtools intersect -abam "+bamFile+" -b "+infile+" > "+infile+"_reads.bam")        

def makeSam():
    path = "."
    for infile in glob.glob(os.path.join(path,'*.bed_reads.bam')):
        commands.getstatusoutput("samtools view "+infile+" > "+infile+".sam")
     
        
def makeUniqSam():
    path = "."
    for infile in glob.glob(os.path.join(path,"*.bam.sam")):
        commands.getstatusoutput("awk '{if (!seen[$2,$10]) {print}; seen[$2,$10]=1}' "+infile+" > "+infile+"_uniq.sam")
    [os.rename(f,f.replace(".bed_reads.bam.sam_uniq.sam","_uniq.sam")) for f in os.listdir(path) if not f.startswith(".")]    
 
def processVariants(variantsFile,bamFile):
    makeFile(variantsFile)
    intersect(bamFile)
    makeSam()
    makeUniqSam()        


### RUN THE PROCESS HERE BY CHANGING THE NAMES OF THE FILES. BE SURE TO PUT THE CODE IN THE SAME FOLDER. PATH SHOULD BE LOCAL ###

processVariants("HCC1954_variants.txt","R_2012_04_10_18_30_53_user_DEF-11-Ampliseq-cancer2.0_ampliseq-sample12-0051_8.bam")
