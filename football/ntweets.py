from ranktweets import *

for i in range(248):
    ranktweets[i][i]=float(ranktweets[i][i])
    a=ranktweets[i][i]
    for j in range(248):
        ranktweets[i][j]=float(ranktweets[i][j])
        b= ranktweets[i][j]
        ranktweets[i][j]=b/a
        #print (ranktweets[i][j])
        
print (ranktweets)
