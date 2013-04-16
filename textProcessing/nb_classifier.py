# Author: Nitesh Turaga
# Graduate student at Carnegie Mellon University
# Naive Bayes Classifier


from collections import Counter
import math
import numpy
import os
import re
import sys
import copy
import operator


"""
Training function: This function trains the classifier based on the 
    training set given.
"""
def trainingFunction(fileNames):

    distinct_words_lib = []
    distinct_words_con = []
    
    n_lib = 0
    n_con = 0
    f = 2
    
    for i in xrange(len(fileNames)):
        if ("lib" in fileNames[i]):
            n_lib +=1
            pathName = "data/" + fileNames[i]
            x = open(pathName)
            libFile = x.read()
            x.close()
            words = libFile.splitlines()
            words = filter(None,words)
#            words = filter("",words)
            distinct_words_lib+=words
        

        if ("con" in fileNames[i]):
            n_con +=1
            pathName = "data/" + fileNames[i]
            x = open(pathName)
            conFile = x.read()
            x.close()
            words = conFile.splitlines()
            words = filter(None,words)
            distinct_words_con+=words

    # Now get the counts and store the words in a dictionary,
    # dict = (Key : word, value: count)
   
    distinct_words_lib = dict(Counter(distinct_words_lib))
    distinct_words_con = dict(Counter(distinct_words_con))
      
    # Merge the words of liberal and consevative together
    vocabulary_full = dict(Counter(distinct_words_lib) + Counter(distinct_words_con))
    # full size of vocabulary, this is |Vocabulary|
    vocabulary_full_sum = len(vocabulary_full)
    vocabulary_lib = sum(distinct_words_lib.values())
    vocabulary_con = sum(distinct_words_con.values())
   
    denominator_lib = vocabulary_lib + vocabulary_full_sum
    denominator_con = vocabulary_con + vocabulary_full_sum
    

    for key in distinct_words_lib:
        distinct_words_lib[key] = float(distinct_words_lib[key] + 1.0)/float(denominator_lib)

    for key in distinct_words_con:
        distinct_words_con[key] = float(distinct_words_con[key] + 1.0)/float(denominator_con)

    newDict = set(distinct_words_con).intersection(distinct_words_lib)

    newDict = list(newDict)

    logDict = {}
  
    for i in xrange(len(newDict)):
        logDict[newDict[i]] = math.log(float(1)/(float(distinct_words_lib[newDict[i]])/float(distinct_words_con[newDict[i]])))
    logDict_sorted  = sorted(logDict,key = logDict.get,reverse = True)[:20]
    
    total_files = n_lib + n_con
    prior_lib = float(n_lib)/float(total_files)
    prior_con = float(n_con)/float(total_files)

    return (prior_con,prior_lib,distinct_words_con,distinct_words_lib,denominator_con,denominator_lib)


"""
    Classifier: this function builds my table of conditional independence based on the test data.
"""
def classifyBlog(pathName,dict_con,dict_lib,prior_con,prior_lib,denominator_con,denominator_lib):
    
    a = open(pathName)
    testData = a.read()
    a.close()

    result_lib = math.log(prior_lib)
    result_con = math.log(prior_con)
    lines = testData.splitlines()
    for line in lines:
        if ((not dict_lib.has_key(line) and (not dict_con.has_key(line)))):
            continue
        if (dict_lib.has_key(line)):
            result_lib = result_lib + math.log(dict_lib[line])
        else:
            result_lib = result_lib +  math.log(float(1)/float(denominator_lib))

        if (dict_con.has_key(line)):
            result_con = result_con + math.log(dict_con[line])
        else :
            result_con =result_con + math.log(float(1)/float(denominator_con))
    
    result_con = result_con +  math.log10(prior_con)
    result_lib = result_lib +  math.log10(prior_lib)

    label = ""
    if (result_lib > result_con):
        label += "L"
    if (result_con > result_lib):
        label += "C"
    return (pathName,label)

"""
Run the total function based on the training and the test set.    
"""

def classifier(train,test):
    
    trainFile = "split/" + train
    testFile = "split/" + test
    
    x = open(trainFile)
    text = x.read()
    x.close()
    
    fileNames =text.split("\n")
    
    (prior_con,prior_lib,dict_con,dict_lib,denominator_con,denominator_lib) = trainingFunction(fileNames)
    
    y = open(testFile)
    testBlogs = y.read()
    y.close()
    
    testFileNames = testBlogs.splitlines()
    z = open("result.txt","w")
    resultStr = ""
    for i in xrange(len(testFileNames)):
        pathName = "data/" + testFileNames[i]
        if (pathName == "data/"): continue
        (testFileNames[i],label) = classifyBlog(pathName,dict_con,dict_lib,prior_con,prior_lib,denominator_con,denominator_lib)
        resultStr += testFileNames[i][5:] +"\t" + label + "\n"
    z.write(resultStr)
    z.close()
    return


"""
Usage: python nb_classifier.py splitX.train splitX.test
    
"""

train = sys.argv[1]
test = sys.argv[2]

classifier(train,test)


