from rankmentions import *

for i in range(248):
    rankmentions[i][i]=float(rankmentions[i][i])
    a=rankmentions[i][i]
    for j in range(248):
        rankmentions[i][j]=float(rankmentions[i][j])
        b= rankmentions[i][j]
        rankmentions[i][j]=b/a
        #print (ranktweets[i][j])
        
print (rankmentions)
