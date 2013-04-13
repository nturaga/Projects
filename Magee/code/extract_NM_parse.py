# Author : Nitesh Turaga

from xml.dom.minidom import parseString
#all these imports are standard on most modern python implementations
 
#open the xml file for reading:
file = open('test.xml','r')
#convert to string:
data = file.read()
#close file because we dont need it anymore:
file.close()
#parse the xml you got from the file
dom = parseString(data)
#retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:
NM_list =""
print "count_from:",dom.getElementsByTagName('Seq-interval_from')[0]
print "count_to:",dom.getElementsByTagName('Seq-interval_from')[-1]
for i in xrange(225):
    xmlTag = dom.getElementsByTagName('Gene-commentary_accession')[i].toxml()
    xmlTag2 = dom.getElementsByTagName('Seq-interval_from')[0].toxml()
    xmlTag3 = dom.getElementsByTagName('Seq-interval_to')[0].toxml()
#strip off the tag (<tag>data</tag>  --->   data):
    xmlData=xmlTag.replace('<Gene-commentary_accession>','').replace('</Gene-commentary_accession>','')
    xmlData2 = xmlTag2.replace('<Seq-interval_from>','').replace('</Seq-interval_from>','')
    xmlData3 = xmlTag3.replace('<Seq-interval_to>','').replace('</Seq-interval_to>','')
    NM_list+=xmlData
    NM_list+="\t"
    NM_list+=xmlData2
    NM_list+="\t"
    NM_list+=xmlData3
    NM_list+= "\n"
#print out the xml tag and data in this format: <tag>data</tag>
#just print the data
print NM_list
