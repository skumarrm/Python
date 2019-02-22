a=[]
index=0

for i in range(1000):
    a.insert(index,i)
    index=index+1
    if index==1000:
        print(a)
    else:
        continue

