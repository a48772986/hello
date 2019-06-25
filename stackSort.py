def LEFT(i):
    return 2*i
def RIGHT(i):
    return 2*i+1
def PARENT(i):
    return i/2
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
              
arr = [1,85,45,23,52,84,54,2,5,3,4,5,6,15,16,34,79,45,7,8]
buildHeap(arr,len(arr)-1)
#heapSort(arr)

print arr
