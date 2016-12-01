import sys
from rankfollowedby import *
from rankfollows import *
from ranklist import *
from ranklistmerged import *
from rankmentionedby import *
from rankmentions import *
from rankretweetedby import *
from rankretweets import *
from ranktweets import *
from quick_sort import *
import numpy as np

neighbour=[]
i=0
for i in range(348):
    user=[]
    user.append(rankfollowedby[i])
    user.append(rankfollows[i])
    user.append(ranklist[i])
    user.append(ranklistmerged[i])
    user.append(rankmentionedby[i])
    user.append(rankmentions[i])
    user.append(rankretweetedby[i])
    user.append(rankretweets[i])
    user.append(ranktweets[i])

    u,s,v = np.linalg.svd(user)
    #print u.shape
    #print s.shape
    #print v.shape
    
    n=[]
    for j in range(348):
        n.append(v[0][j])
    neighbour.append(n)
#print(neighbour)
#print (len(neighbour))
#print (len(neighbour[0]))

kk=0
rank=[]
for i in range(len(neighbour)):
    L=neighbour[i]
    index=[j+1 for j in range(348)]
    quickSort(L,0,347,index)
    #ranking=[0 for j in range(464)]
    #for j in range(0,464):
    #   kk=j+1
    #   ranking[index[j]-1]=kk
    rank.append(index)


f=open('neighbour.py','w')
sys.stdout=f
print(rank)
f.close
