# def check_duplicate(nums):
#     if len(nums) != len(set(nums)):
#         print("Duplicate Found")

# check_duplicate([1,2,3,4,5])

# implementing stack using list

# stack=[]
# def append():
#     if len(stack)==n:
#         print("stack if full")
#     ele=int(input("Enter element"))
#     stack.append(ele)
#     print(stack)

# def pop():
#     if len(stack)==0:
#         print("stack is empty")
#     else:
#         a=stack.pop()
#         print(stack)
#         print("pop element is",a)

# n=int(input("Enter the stack size or limit"))        
# while True:
#     choice=input("Enter operation no. 1.push,2.Pop,3.exit")
#     b=int(input("Enter the number"))
#     if b == 1:
#         append()
#     elif b == 2:
#         pop()
#     elif b == 3:
#         break
#     else:
#         print("Invalid choice")


# stack using modules 

# from collections import deque
# stack=deque()
# stack.append(1)
# stack.append(2)
# print(stack)
# stack.pop()
# print(stack)

from queue import LifoQueue
stack=LifoQueue()  # lifoqueue is class which is used to implement stack
stack.put(1)  # put is used to add element in stack
stack.put(2)
stack.put(3)
print(stack)          # it gives object reference because it doesnot exposed internal element directly,use get to access element
stack.get()   # get is used to remove element from stack
print(stack)
stack.full()  # to check if the stack is full or not
print(stack.empty())