from rankmentionedby import *

for i in range(248):
    rankmentionedby[i][i]=float(rankmentionedby[i][i])
    a=rankmentionedby[i][i]
    for j in range(248):
        rankmentionedby[i][j]=float(rankmentionedby[i][j])
        b= rankmentionedby[i][j]
        rankmentionedby[i][j]=b/a
        #print (ranktweets[i][j])
        
print (rankmentionedby)
