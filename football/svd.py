import sys
from normfollowedby import *
from normfollows import *
from normlist import *
from normlistmerged import *
from normmentionedby import *
from normmentions import *
from normretweetedby import *
from normretweets import *
from normtweets import *
from quick_sort import *
import numpy as np

neighbour=[]
i=0
for i in range(248):
    user=[]
    user.append(normfollowedby[i])
    user.append(normfollows[i])
    user.append(normlist[i])
    user.append(normlistmerged[i])
    user.append(normmentionedby[i])
    user.append(normmentions[i])
    user.append(normretweetedby[i])
    user.append(normretweets[i])
    user.append(normtweets[i])

    u,s,v = np.linalg.svd(user)
    #print u.shape
    #print s.shape
    #print v.shape
    
    n=[]
    for j in range(248):
        n.append(v[0][j])
    neighbour.append(n)
#print(neighbour)
#print (len(neighbour))
#print (len(neighbour[0]))

kk=0
rank=[]
for i in range(len(neighbour)):
    L=neighbour[i]
    index=[j+1 for j in range(248)]
    quickSort(L,0,247,index)
    #ranking=[0 for j in range(248)]
    #for j in range(0,248):
    #   kk=j+1
    #   ranking[index[j]-1]=kk
    rank.append(index)


f=open('neighbour.py','w')
sys.stdout=f
print(rank)
f.close
