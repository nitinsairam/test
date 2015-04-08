'''
Created on Mar 17, 2015
sample.txt = The Apache Hadoop software library is a framework 
that allows for the distributed processing of large data sets 
across clusters of computers using simple programming models. 
It is designed to scale up from single servers to thousands of machines, 
each offering local computation and storage. 
Rather than rely on hardware to deliver high-availability, 
the library itself is designed to detect and handle failures at the 
application layer, so delivering a highly-available service on top of a cluster 
of computers, each of which may be prone to failures.

@author: Nitin
'''

''' sample word count program in python'''

file = open("D:/sample.txt","r")
count=0
#for line in file:
    #for word in line.split():
        #print word,count
        #count+=1

#for word in file.read().split():
    #count+=1
    #print word,count

print"Total number of words",count