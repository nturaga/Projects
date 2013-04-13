
def eliminateSpace(text):
    if (text == None):
        return None
    edited = ""
    for i in xrange(len(text)):
        if text[i]==text[i-1] and str.isspace(text[i])==True:
            continue
        edited+=text[i]
    return edited


def mainFunction(textnm,texthg):
    newStr=""
    for i in xrange(len(textnm)):
        for j in xrange(len(texthg)-1):
            #print texthg[j]
            if textnm[i] in texthg[j].split("\t"):
#            #extract strat and end positions here
                lineHG_array = texthg[j].split("\t")
                newStr+=lineHG_array[0]
                newStr+="\t"
                newStr+=textnm[i]
                newStr+="\t"
                if (lineHG_array[5] == '+'):
                    newStr+=lineHG_array[1]
                else:
                    newStr+=lineHG_array[2]
                newStr+="\n"
    return newStr
    


def run():
    file_NM = open("NM_IDs.txt","r")
    text_NM = file_NM.read()
    file_NM.close()

    file_HG = open("hg18.bed","r")
    text_HG = file_HG.read()
    file_HG.close()

    #Array for NM_ID's--Size is 4291
    textnm = text_NM.split("\n")

    #Array for the HG chromosomes
    texthg = text_HG.split("\n")
#    print len(texthg)
    out_handle = open("TSS_TTS.txt","w")
    
    out_handle.write(mainFunction(textnm,texthg))
    return 
    
run()
