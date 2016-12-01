from rankretweets import *

for i in range(248):
    rankretweets[i][i]=float(rankretweets[i][i])
    a=rankretweets[i][i]
    for j in range(248):
        rankretweets[i][j]=float(rankretweets[i][j])
        b= rankretweets[i][j]
        rankretweets[i][j]=b/a
        #print (ranktweets[i][j])
        
print (rankretweets)
