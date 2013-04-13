from Bio import Entrez
from Bio import SeqIO
import os

def readTextFile(filename):
    fileHandler = open(filename, "rt")
    text = fileHandler.read()
    fileHandler.close()
    return text

def readTextFileAsList(filename):
    # readlines includes '\n' characters, so we'll use split() instead
    text = readTextFile(filename)
    #if (text == None):
    #    return None
    return text.split("\n")

id_list = readTextFileAsList("new_test_id.txt")
print "id_list",id_list


Entrez.email = "nitesh.turaga@gmail.com"
for i in xrange(len(id_list)):
    print "i:",i
    net_handle = Entrez.efetch(db = "gene", id = id_list[i],rettype="gb",retmode = "xml")
#    if not os.path.isfile(filename):
    filename = "file_gen%d"%(i)
    out_handle = open(filename,"w")
    out_handle.write(net_handle.read())
    out_handle.close()
    net_handle.close()
    print "Saved"
        
