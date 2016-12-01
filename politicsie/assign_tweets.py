import sys
from ids import *
from quick_sort import *

w=14377
h=348
w1=20
matrix = [[0 for x in range(w)]for y in range(h)]
i=0

with open('politicsie-tweets500.mtx') as f:
    for line in f:
        if i==0:
            i=i+1
            continue
       
        s=line[:-1]
        L=s.split(' ')
        matrix[int(ids[L[1]])][int(L[0])]=L[2]

#print(matrix)

a,b=348,348
sim = [[0 for x in range(a)]for y in range(b)]

for i in range(a):
    for j in range(i+1,a):
        for k in range(w):
            sim[i][j]=sim[i][j]+float(matrix[i][k])*float(matrix[j][k])
        sim[j][i]=sim[i][j]
        if i!=j and sim[i][j]==0:
            sim[i][j]=-1
            sim[j][i]=-1
#print(sim)
kk=0
rank=[]
for i in range(a):
    j=0
    index=[j+1 for j in range(348)]
    L=sim[i]
    count=0
    j=0
    for j in range(348):
        if sim[i][j]>0:
            count=count+1
    count=count+1
    quickSort(L,0,347,index)
    #index.remove(i)
    ranking=[0 for j in range(348)]
    j=0
    end=count+1
    if end==a+1 :
        end=end-1
    end=float(end)
    for j in range(0,348):
        
        if L[j]==-1:
            ranking[index[j]-1]=count/end
        elif index[j]-1==i :
            ranking[index[j]-1]=end/end
        else:
            kk=j+1
            ranking[index[j]-1]=kk/end
    
    rank.append(ranking)

#f=open('ranktweets.py','w')
#sys.stdout=f
print(rank)
#f.close()

