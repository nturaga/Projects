# Author: Nitesh Turaga
# Systems Programmer II, Lab - Adrian lee, Magee Womens Research Institute

# Description: count NM accession numbers in generatedfile.bed


import math
import numpy as np

def run():
    
    file1 = open("TSS_TTS_unique.txt","r")
    NMs = file1.read()
    file1.close()
    
    file = open("ER_only_formatted.txt","r")
    genFile = file.read()
    file.close()

    edited = countNMs(NMs,genFile)

    x = open("NMs_counts_ER_only.txt","wt")
    x.write(edited)
    x.close()
    return


def countNMs(NM,gen):
    edited =""
    for NM_line in NM.splitlines(): 
            
        NM_counter = 0
        distance = []
            
        for gen_line in gen.splitlines():
            
        # If the chromosomes name is the same
            gen_line_array = gen_line.split("\t")
            NM_line_array = NM_line.split("\t")
            
            if ((NM_line_array[0] == gen_line_array[0])):
            #Then check the NM IDS 
            # If the NM_Id is in the line of the gen_file
                if (NM_line_array[1] in gen_line_array):
                    print "ENTERING"
                    edited += NM_line_array[1]
                    edited +="\t"
                    for i in xrange(len(gen_line_array)):
                        if (gen_line_array[i] == "\t"):
                            break
                    
                        elif (gen_line_array[i] == NM_line_array[1]):
                            NM_counter+=1
                            distance.append(abs(float(gen_line_array[i+1])))
            edited+=str(NM_counter)
            edited+="\t"
            median_distance = np.median(distance)
            edited += str(median_distance)
            edited+="\t"
            if (len(distance)>0):
                edited+=str(min(distance)) 
            edited+="\n"
    return edited

run()




                            
