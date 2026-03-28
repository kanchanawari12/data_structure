# implementing queue using list
# adding and removing elements in queue is called as enqueue and dequeue respectively
# queue=[]
# def enqueue():   #push
#     ele=int(input("Enter element "))
#     queue.append(ele)
#     print(queue)

# def dequeue():    #pop
#     if len(queue)==0:
#         print("queue is empty")
#     else:
#         queue.pop(0) # pop(0) is used to remove the first element from the queue
#         print(queue)


# while True:
    # choice=input("Operations tobe Perform 1.enqueue,2.dequeue,3.exist")
    # num=int(input("Enter the Operation number "))
    # if num==1:
    #     enqueue()
    # elif num==2:
    #     dequeue()
    # elif num==3:
    #     break
    # else:
    #     print("Enter valid number")

#queue implementation using modules
# from collections import deque
# queue=deque()
# queue.append(1)
# queue.append(2)
# print(queue)
# queue.popleft()  # popleft is used to remove the first element from the queue
# print(queue)     

# implementing queue using queue module
# from queue import Queue
# q=Queue()
# q.put(1)  # to add element in queue we use put() method
# q.put(2)  
# print(q.get()) # to remove element from queue we use get() method
# print(q.get())
# print(q.full())  # to check if the queue is full or not
# print(q.empty()) # to check if the queue is empty or not


#implenting priority queue using queue module
#here lowest element have highest priority so it will remove first
# from queue import PriorityQueue
# pq=PriorityQueue()
# pq.put(4)
# pq.put(10)
# pq.put(2)
# pq.put(1)
# print(pq.get())
# print(pq.get())
# print(pq.get())
# print(pq.get())
# #using tuple we can also implement priority queue
# pq.put((2,"shubh"))
# pq.put((10,"kanchan"))
# pq.put((3,"kanchan"))
# print(pq.get())
# print(pq.get())
# print(pq.get())

#implemnting priority queue using list
pq=[]
pq.append(1)
pq.append(10)
pq.append(11)
pq.append(20)
print(pq)
pq.sort()
print(pq.pop(0))
print(pq.pop(0))
