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
    #for infile in glob.glob(os.path.join(path,"*_uniq.sam")):
    [os.rename(f,f.replace(".bed_reads.bam.sam_uniq.sam","_uniq.sam")) for f in os.listdir(path) if not f.startswith(".")]    
 
def processVariants(variantsFile,bamFile):
    makeFile(variantsFile)
    intersect(bamFile)
    makeSam()
    makeUniqSam()        


#makeFile("RH02-Somatic_Variants.txt")

### RUN THE PROCESS HERE BY CHANGING THE NAMES OF THE FILES. BE SURE TO PUT THE CODE IN THE SAME FOLDER. PATH SHOULD BE LOCAL ###

processVariants("HCC1954_variants.txt","R_2012_04_10_18_30_53_user_DEF-11-Ampliseq-cancer2.0_ampliseq-sample12-0051_8.bam")



#processVariants("RH01_Somatic_Variants.txt","R_2012_06_07_17_34_13_user_DEF-23-ALee_Ampliseq_RH01_6-7-12_Auto_DEF-23-ALee_Ampliseq_RH01_6-7-12_20.bam")
#processVariants("RH02-Somatic_Variants.txt","R_2012_06_08_16_57_42_user_DEF-25-ALee_Ampliseq_RH02_6-8-12_Auto_DEF-25-ALee_Ampliseq_RH02_6-8-12_22.bam")
#processVariants("RH03_variants.txt","R_2012_06_08_13_18_52_user_DEF-24-ALee_Ampliseq_RH03_6-8-12_Auto_DEF-24-ALee_Ampliseq_RH03_6-8-12_21.bam")
#processVariants("RH04_variants.txt","R_2012_06_07_14_29_53_user_DEF-22-ALee_Ampliseq_RH04_6-7-12_Auto_DEF-22-ALee_Ampliseq_RH04_6-7-12_19.bam")
#processVariants("RH05_variants.txt","R_2012_05_15_17_58_36_user_DEF-17-12-0119-05-15-12_12_0119-rh05_051612.bam")
#processVariants("RH07_variants.txt","R_2012_05_16_17_50_20_user_DEF-18-ALee_Ampliseq_12-0120_RH07_5_16_2012_Ampliseq_12-0120RH07_5-22-2012v22.bam")
#processVariants("RH08_variants.txt","R_2012_06_06_15_13_24_user_DEF-21-ALee_Ampliseq_RH08_6-6-12_Auto_DEF-21-ALee_Ampliseq_RH08_6-6-12_18.bam")
#processVariants("RH09_variants.txt","R_2012_06_13_16_03_39_user_DEF-26-ALee-Ampliseq_RH09_6-13-12_Auto_DEF-26-ALee-Ampliseq_RH09_6-13-12_23.bam")
#processVariants("RH10_variants.txt","R_2012_06_05_16_04_56_user_DEF-20-ALee_Ampliseq_RH10_6-5-12_Auto_DEF-20-ALee_Ampliseq_RH10_6-5-12_17.bam")
#processVariants("RH21_variants.txt","R_2012_05_17_17_06_54_user_DEF-19-12-0124-rh21-5-17-2012_Auto_DEF-19-12-0124-rh21-5-17-2012_16.bam")
