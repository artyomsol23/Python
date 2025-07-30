class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def heapify_down(self, i):
        while True:
            left = self.left_child(i)
            right = self.right_child(i)
            smallest = i
            
            if left < self.size and self.heap[left] < self.heap[smallest]:
                smallest = left
            
            if right < self.size and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            if smallest == i:
                break
                
            self.swap(i, smallest)
            i = smallest
    
    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.heapify_up(self.size - 1)
    
    def extract_min(self):
        if self.size == 0:
            return None
        
        min_item = self.heap[0]
        self.size -= 1
        last_item = self.heap.pop()
        
        if self.size > 0:
            self.heap[0] = last_item
            self.heapify_down(0)
        
        return min_item
    
    def get_min(self):
        return self.heap[0] if self.size > 0 else None
    
    def size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size
    
    def __bool__(self):
        return self.size > 0
