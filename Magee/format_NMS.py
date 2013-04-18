# Author: Nitesh Turaga
# Systems Programmer II, Lab - Adrian lee, Magee Womens Research Institute

# Description:

def run():
    file = open("NM_counts_ER_only_norepeats.txt","r")
    text = file.read()
    file.close()

    x = open("NM_counts_ER-only_formatted.txt","wt")
    x.write(format(text))

    return 

def format(text):
    edited=""
    lines = text.split("\n")    
    i=1
    while(i<len(lines)-1):
        NM_id = lines[i].split("\t")[0]
        counter = text.count(NM_id)
        tofind = "%s\t%s"% (str(NM_id),str(counter))
        for line in open("NM_counts_ER_only_norepeats.txt"):
            if tofind in line:
                edited+=line
        i+=counter
    return edited

run()

