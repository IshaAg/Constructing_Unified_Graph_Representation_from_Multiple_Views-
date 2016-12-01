import sys


ids={}
users=248
i=0
with open('olympics.ids') as f:
    for line in f:
        #Removing the end character
        s=line[:-1]
        ids[s]=i
        print(i)
        i=i+1
f=open('ids.py','w')
sys.stdout=f
print(ids)
f.close()
