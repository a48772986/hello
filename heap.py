class my_heap(object):
    def __init__(self, heap, flag):
        self.flag = flag
        self.heap = heap
    def parent(self, i):
        return (i-1)/2
    def left(self, i):
        return 2*i+1
    def right(self, i):
        return 2*i+2
    def up(self, i):
        if i == 0:
            return
        p = self.parent(i)
        temp_val = i
        if self.flag == 0:
            if self.heap[p] < self.heap[temp_val]:
                temp_val = p
        elif self.flag == 1:
            if self.heap[p] > self.heap[temp_val]:
                temp_val = p
        if temp_val != i:
            self.heap[i],self.heap[temp_val] = self.heap[temp_val],self.heap[i]
            self.up(temp_val)
    def down(self, i):
        if i > len(self.heap)-1:
            return
        l = self.left(i)
        r = self.right(i)
        temp_val = i
        if l < len(self.heap):
            if self.flag == 0:
                if self.heap[l] > self.heap[temp_val]:
                    temp_val = l
            elif self.flag == 1:
                if self.heap[l] < self.heap[temp_val]:
                    temp_val = l
        if r < len(self.heap):
            if self.flag == 0:
                if self.heap[r] > self.heap[temp_val]:
                    temp_val = r
            elif self.flag == 1:
                if self.heap[r] < self.heap[temp_val]:
                    temp_val = r
        if temp_val != i:
            self.heap[i],self.heap[temp_val] = self.heap[temp_val],self.heap[i]
            self.down(temp_val)
    def insert(self, val):
        self.heap.append(val)
        size = len(self.heap) - 1
        #print size
        self.up(size)
    def heappop(self):
        self.heap[0],self.heap[-1] = self.heap[-1],self.heap[0]
        out = self.heap.pop()
        self.down(0)
        return out
my_heap = my_heap([],0)
my_heap.insert(6)
my_heap.insert(3)
my_heap.insert(8)
my_heap.insert(1)
my_heap.insert(9)
my_heap.insert(0)
my_heap.insert(7)
print my_heap.heap
print my_heap.heappop()
print my_heap.heap
print my_heap.heappop()
print my_heap.heap
print my_heap.heappop()
print my_heap.heap
print my_heap.heappop()
print my_heap.heap
