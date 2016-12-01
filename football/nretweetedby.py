from rankretweetedby import *

for i in range(248):
    rankretweetedby[i][i]=float(rankretweetedby[i][i])
    a=rankretweetedby[i][i]
    for j in range(248):
        rankretweetedby[i][j]=float(rankretweetedby[i][j])
        b= rankretweetedby[i][j]
        rankretweetedby[i][j]=b/a
        #print (ranktweets[i][j])
        
print (rankretweetedby)
