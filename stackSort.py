def LEFT(i):
    return 2*i+1
def RIGHT(i):
    return 2*i+2
def PARENT(i):
    return (i-1)/2
def maxHeap(A,i,size):
    l = LEFT(i)
    r = RIGHT(i)
    largest = i
    if l <= size:
        if A[l] > A[largest]:
            largest = l
    if r <= size:
        if A[r] > A[largest]:
            largest = r
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        maxHeap(A,largest,size)
def buildHeap(A, size):
    for i in range(size/2,-1,-1):
        maxHeap(A,i,size)
def heapSort(A):
    size = len(A) -1
    buildHeap(A, size)
    for i in range(size,0,-1):
        A[0],A[i] = A[i],A[0]
        size = size-1
        maxHeap(A,0,size)
def upHeap(A,i,size):
    l = LEFT(i)
    r = RIGHT(i)
    p = PARENT(i)
    largest = i
    if l <= size:
        if A[l] > A[largest]:
            largest = l
    if r <= size:
        if A[r] > A[largest]:
            largest = r
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        if i == 0:
            return
        else:
            upHeap(A, p, size)
def insert(A,val):
    A.append(val)
    size = len(A)-1
    i = PARENT(size)
    
    upHeap(A, i, size)
printh = {}
def printHeap(A, i, count):
    if i < len(A):
        if count not in printh:
            printh[count] = []
        printh[count].append(A[i])
        count += 1
        printHeap(A, LEFT(i), count)
        printHeap(A, RIGHT(i), count)
arr = [1,85,45,23,52,84,54,2,5,3,4,5,6,15,16,34,79,45,7,8]
buildHeap(arr,len(arr)-1)
#heapSort(arr)

print arr

insert(arr,99)

printHeap(arr, 0, 0)
for i in printh:
    print printh[i],i
