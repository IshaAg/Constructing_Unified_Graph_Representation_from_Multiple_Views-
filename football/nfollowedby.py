from rankfollowedby import *

for i in range(248):
    rankfollowedby[i][i]=float(rankfollowedby[i][i])
    a=rankfollowedby[i][i]
    for j in range(248):
        rankfollowedby[i][j]=float(rankfollowedby[i][j])
        b= rankfollowedby[i][j]
        rankfollowedby[i][j]=b/a
        #print (ranktweets[i][j])
        
print (rankfollowedby)
