# Author: Nitesh Turaga
# Systems Programmer II, Lab - Adrian lee, Magee Womens Research Institute

# Description:

import re
import commands
import os
import glob
from xml.dom.minidom import parseString

count = 0
MainName = "HCC1954"

for line in open(MainName+"_variants.txt"):
    count +=1
    start = str(int(line.split("\t")[1])-25)
    stop = str(int(line.split("\t")[2])+25)
    chrom = line.split("\t")[0]
    chr = chrom[3:]
    print chr,start,stop
    saveFile = "%d_%s_das.txt" % (count,line.split("\t")[3])
    commands.getstatusoutput("curl http://genome.ucsc.edu/cgi-bin/das/hg19/dna?segment="+chr+":"+start+","+stop+"  > "+saveFile+"")


for infile in glob.glob(os.path.join(".","*_das.txt")):
    x = open(infile,"r")
    text = x.read()
    x.close()
    #count = 0
    seq = ""
    f = text.split("\n")
    seq = f[5]+f[6]
    positionLine = text.split("\n")[3]
    #START
    startArray = positionLine.split(" ")[2].split("=")
    startPos = startArray[1].replace("\"","")
    #STOP
    stopArray = positionLine.split(" ")[3].split("=")
    stopPos = stopArray[1].replace("\"","")

    name = "%s_seq.txt" % (infile)
    file = open(name,"wt")
    writeLine = "%s\t%s\t%s" % (seq,startPos,stopPos)
    file.write(writeLine)


filename = MainName+"_seq"
commands.getstatusoutput("mkdir "+filename+"")
commands.getstatusoutput("mv *_das.txt_seq.txt "+filename+"")


