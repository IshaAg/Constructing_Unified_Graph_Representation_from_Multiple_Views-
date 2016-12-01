from ranklist import *

for i in range(248):
    ranklist[i][i]=float(ranklist[i][i])
    a=ranklist[i][i]
    for j in range(248):
        ranklist[i][j]=float(ranklist[i][j])
        b= ranklist[i][j]
        ranklist[i][j]=b/a
        #print (ranktweets[i][j])
        
print (ranklist)
