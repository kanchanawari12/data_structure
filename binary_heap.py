import heapq
# Binary Heap implementation using Python's built-in heapq module
'''
heapq is python module which uses binary heap data structure to implement a priority queue and min-heap
it provide various function to perform heap operations like push, pop, peek, etc.
'''
# using list to represent the binary heap
heap=[]
heapq.heappush(heap,10)
heapq.heappush(heap,9)
heapq.heappush(heap,8)
heapq.heappush(heap,1)
heapq.heappush(heap,11)
print(heap) 

heapq.heappop(heap)   # it will return smallest value from heap and delete it from heap
print(heap)
heapq.heappushpop(heap,5)   # it will push the new value and pop the smallest value from heap
print(heap)
heapq.heapreplace(heap,100)   # it will pop the smallest value and push the new value to heap
print(heap)
heapq.heapify(heap)     # it will convert the list into a heap
print(heap)
heapq._heapify_max(heap)     # it will convert the list into a max heap
print(heap)
print(heapq.nsmallest(3,heap))   # it will return the 3 smallest value from heap and it will not modify the heap
print(heapq.nlargest(3,heap))    # it will return the 3 largest value from heap and it will not modify the heap 
print(heap)