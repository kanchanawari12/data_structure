print("1st pattern")
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()         # it will print a pattern of stars and it will print a new line after each row of stars

print("2nd pattern")

for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()         # it will print a pattern of stars in reverse order and it will print a new line after each row of stars

print("3rd pattern")
for i in range(1,6):
    print(" "*(5-i),end="")
    print("* "*i)

print("4th pattern")
for j in range(5,0,-1):
    print(" "*(5-j),end="")
    print("* "*j)

print("5th pattern")
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("6th pattern")
for i in range(1,5):
    print((str(i)+" ")*i)

print("7th pattern")
sum=0
for i in range(1,6):
    for j in range(1,i+1):
      sum=sum+j
      print(sum,end=" ")
    print()

print("8th pattern")
n=4
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

print("9th pattern")
for i in range(1,6):
    print("* "*i)

for i in range(1,6):
    print(" "*(5-i),end="")
    print("* "*i)

for i in range(5,0,-1):
    print("* "*i)

print("10th pattern")
for i in range(1,6):
    for j in range(i,6):
        print(" ",end="")
    for k in range(1,i+1):
        print("* ",end="")
    print()

print("11th pattern")
for i in range(1,6):
    for j in range(i,6):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    for l in range(i+1):
        print("*",end="")
    print()

   
