# def decorator(func):
#     def start_transaction():
#         print("Transaction started")
#         func()
#         print("Transaction completed")
#     return start_transaction

# @decorator
# def transaction():
#     print("Transaction in progress")

# transaction()



# # generators in pyhton

# def generator():
#     for i in range(10):
#         if:
#             yield i
#         else:
#             print("Generator completed")

# g=generator()
# print(next(g))
# print(next(g))
# print(next(g))


# i want to print 5-1 numbers 
# num=5
# def generator(num):
#     for i in range(num,0,-1):
#         yield i




# num=int(input("Enter the number "))
# for i in range(num,0,-1):
#     print(i)

#using if condition and without using loop
# num=int(input("Enter the number "))


# n=5655
# rev=0
# a=n//10  # removes the last digit
# b=n%10   # gives the last digit
# rev=rev*10+b  # adds the last digit to the reverse number
# n=a  # removes the last digit from the original number
# print(rev)

# def reverse_number(n,rev=0):
#     if n==0:
#         return rev
#     return reverse_number(n//10,rev*10+n%10)      # recursive call to the function with the updated values of n and rev

# def return_reverse_number(n,rev=0):
#     while True:
#         a=n//10
#         b=n%10
#         rev=rev*10+b
#         n=a
#         if n==0:
#             return rev
        
# print(return_reverse_number(5655))

# def reverse_string(s,rev=0):
#     while True:
#         rev=str(rev)+s[-1]
#         s=s[:-1]                 # removes the last character from the string
#         if s=="":
#            rev=rev.lstrip("0")   # removes the leading zeros from the reverse string
#            return rev
        
# print(reverse_string("kanchan"))

str="kanchan"
rev=""
rev=str[::-1]   # slicing the string in reverse order
print(rev)
