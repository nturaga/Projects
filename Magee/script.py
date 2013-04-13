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
    
    #if (count ==6 or count ==7):
    #        seq+=line
    #    count+=1
    name = "%s_seq.txt" % (infile)
    file = open(name,"wt")
    writeLine = "%s\t%s\t%s" % (seq,startPos,stopPos)
    file.write(writeLine)


filename = MainName+"_seq"
commands.getstatusoutput("mkdir "+filename+"")
commands.getstatusoutput("mv *_das.txt_seq.txt "+filename+"")



   
#    r = re.compile("<DNA length=\"52\">\n(.*)\n</DNA>").match(text).groups()
#    print r
#    lyrics = r.group(1)

 #   print lyrics


#    dom = parseString(text)
#    xmlTag = dom.getElementsByTagName('DNA')[0].toxml()
#    xmlData = xmlTag.replace('<DNA length="52">','').replace('</DNA>','')



#import easy to use xml parser called minidom:
#from xml.dom.minidom import parseString
#all these imports are standard on most modern python implementations
 
#convert to string:
#data = file.read()
#close file because we dont need it anymore:
#file.close()
#parse the xml you got from the file
#dom = parseString(data)
#retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:
#xmlTag = dom.getElementsByTagName('tagName')[0].toxml()
#strip off the tag (<tag>data</tag>  --->   data):
#xmlData=xmlTag.replace('<tagName>','').replace('</tagName>','')
#print out the xml tag and data in this format: <tag>data</tag>
#print xmlTag
#just print the data
#print xmlData
