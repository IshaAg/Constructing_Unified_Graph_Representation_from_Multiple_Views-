import sys


ids={}
users=348
i=0
with open('politicsie.ids') as f:
    for line in f:
        #Removing the end character
        s=line[:-1]
        ids[s]=i
        #print(i)
        i=i+1
f=open('ids.py','w')
sys.stdout=f
print(ids)
f.close()
