import math

def run():
    file1 = open("genFle.bed","r")
    ER_E2 = file1.read()
    file1.close()
    
    file2 = open("SRC1-E2_BED_MACS_1e-5_peaks.bed","r")
    SRC = file2.read()
    file2.close()
    
    #Fill in the return values
    (returnedText1,returnedText2) = compare(ER_E2,SRC)
    
    writeFile1 = open("ER_SRC_1.txt","wt")
    writeFile1.write(returnedText1)
    
    writeFile2 = open("ER_only.txt","wt")
    writeFile2.write(returnedText2)
    
    return 


def compare(ERE2, SRC_1):
    
    ERE2_SRC_text = ""
    ER_text = ""
    
    for line_ERE2 in ERE2.splitlines():
#        print "line_ERE2",line_ERE2
        ERE2_split = line_ERE2.split("\t")
#        print "ERE2_split[0]",ERE2_split[0]
        for line_SRC in SRC_1.splitlines():
#            print "line_SRC",line_SRC
            SRC_split = line_SRC.split("\t")
#            print "SRC_split[0]",SRC_split[0]
            if (ERE2_split[0] == SRC_split[0]):
                
                if (( (float(SRC_split[1]) >= float(ERE2_split[1]))\
                    and (float(SRC_split[1]) <= float(ERE2_split[2])))\
                    or ( (float(SRC_split[2]) >= float(ERE2_split[1]))\
                    and (float(SRC_split[2]) <= float(ERE2_split[2]))) ):
                        
                        ERE2_SRC_text += line_SRC
                        ERE2_SRC_text +="\n"
#                        print "add1"
                else:
                    ER_text+=line_SRC
                    ER_text+="\n"
#                    print "add2"
    return (ERE2_SRC_text,ER_text)
                    

run()
