from neighbour import *
import sys
edge=[]
k=15
for i in range(len(neighbour)):
    for j in range(0,k):
        t=()
        t=list(t)
        t.insert(0,i+1)
        t.insert(1,neighbour[i][j])
        t=tuple(t)
        edge.append(t)

f=open('graphedges2.py','w')
sys.stdout=f
print(edge)
f.close
