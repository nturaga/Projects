from xml.dom.minidom import parseString

#Open xml file for reading

file = open("filedata.txt","r")

data = file.read()

file.close()

newStr = ""
for line in data.splitlines():
#    print line
    match =  "<Gene-commentary_accession>NM_"
    line = line.strip()
    if line.startswith(match):
 
#       print line
        newStr+=line
        newStr+="\n"


out_handle = open("NM_IDs.txt","w")
out_handle.write(newStr)


