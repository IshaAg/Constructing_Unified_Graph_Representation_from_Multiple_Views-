from ranklistmerged import *

for i in range(248):
    ranklistmerged[i][i]=float(ranklistmerged[i][i])
    a=ranklistmerged[i][i]
    for j in range(248):
        ranklistmerged[i][j]=float(ranklistmerged[i][j])
        b= ranklistmerged[i][j]
        ranklistmerged[i][j]=b/a
        #print (ranktweets[i][j])
        
print (ranklistmerged)
