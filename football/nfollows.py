from rankfollows import *

for i in range(248):
    rankfollows[i][i]=float(rankfollows[i][i])
    a=rankfollows[i][i]
    for j in range(248):
        rankfollows[i][j]=float(rankfollows[i][j])
        b= rankfollows[i][j]
        rankfollows[i][j]=b/a
        #print (ranktweets[i][j])
        
print (rankfollows)
