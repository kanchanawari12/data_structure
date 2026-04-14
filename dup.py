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

# resverse a number
num=1234
rev=0
while num>0:
    a=num%10
    rev=rev*10+a   # it shift digit to left also make space for new digit
    num =  num // 10
print(rev)

# reverse a string
str="kanchan"
rev=""
for i in range(-1,-len(str)-1,-1):
    rev=rev+str[i]
print(rev)