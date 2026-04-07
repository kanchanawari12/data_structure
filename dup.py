list=[1,2,3,4,5,6,7,8,9,10,1,2,3]
li=set()
count=0
duplicate=[]
for i in list:
    if i in li:
        duplicate.append(i)
        count=count+1
    else:
        li.add(i)
        
print(duplicate)
print(count)